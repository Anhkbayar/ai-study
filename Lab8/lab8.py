# 2. Импорт ба тохиргоо
import torch
from transformers import pipeline
import nltk
import sacrebleu
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
from tabulate import tabulate
nltk.download('punkt')

print("Бүгд амжилттай суусан!\n")

# 3. Загвар сонгох (gpt2 маш хурдан, гэхдээ монгол хэл муу. Илүү сайн үр дүн авахыг хүсвэл доорхыг идэвхжүүл)
generator = pipeline("text-generation",
                     model="gpt2",
                     # model="l3cube-pune/mongolian-bert",   #better mongolian
                     device=0 if torch.cuda.is_available() else -1)

prompts = [
    "Монгол хэлний боловсруулалтын ирээдүй ямар байх вэ?",
    "2025–2030 оны хооронд Монгол хэлний байгалийн хэлний боловсруулалт (NLP) ямар чиг хандлага давамгайлах вэ, ямар бэрхшээлүүд гарч болох вэ?",
    "Боловсролын салбарт Монгол хэлний NLP технологийг хэрхэн ашиглаж болох вэ? 3 тодорхой жишээ авч тайлбарла.",
    "Монгол хэлний байгалийн хэлний боловсруулалтын талаар 5 сонирхолтой баримтыг жагсааж бичээрэй.",
    """Few-shot жишээ:
Асуулт: Испани хэлний NLP-ийн гол бэрхшээл юу вэ?
Хариу: Gender, диалект, товчлол ихтэй, субжунктив хэрэглээ нарийн.

Асуулт: Монгол хэлний NLP-ийн гол бэрхшээл ба онцлог юу вэ?""",
    "2035 онд Монгол хэлний NLP хэрхэн хөгжсөнийг төсөөлөөд 250-300 үгтэй жижиг өгүүлэл бичээрэй."
]

references = [
    "Монгол хэлний боловсруулалт ирээдүйд маш хурдацтай хөгжинөд, боловсрол, эрүүл мэнд, төрийн үйлчилгээнд өргөн хэрэглэгдэнэ.",
    "2025–2030 онд монгол хэлний том загварууд (Mongolian LLM) гарч, машин орчуулгын чанар 90% хүрнэ, морфологийн анализаторууд илүү нарийвчлалтай болно. Гол бэрхшээл: сургалтын өгөгдөл хомс, кирилл+уламжлалт бичиг хосолсон байдал.",
    "1. Автомат хичээл боловсруулах систем, 2. Ярианы үнэлгээ өгөх апп, 3. Монгол хэл дээрх дижитал номын сан, ухаалаг хайлт.",
    "1. Агглютинатив хэл, 2. 8 үсгийн аймагтай, 3. Кирилл ба уламжлалт бичиг хосолдог, 4. Дэлхийд өгөгдөл хомс, 5. 2023-2025 онд Mongolian BERT, GPT загварууд гарсан.",
    "Монгол хэл агглютинатив тул нэг үг олон дагавар авдаг, өгөгдөл хомс, хоёр бичигтэй учраас токенчлал хэцүү, гэхдээ сүүлийн жилүүдэд маш их ахиц гарсан.",
    "2035 онд монгол хэлээр ярьдаг хүүхэд роботтой монгол хэлээр ярина, төрийн үйлчилгээ 100% дуут командаар хийгдэнэ, шинжлэх ухааны өгүүлэл монгол хэлээр бичигдэж, дэлхийн шилдэг LLM-тэй өрсөлдөнө."
]

print(f"Нийт {len(prompts)} prompt бэлэн боллоо. Загвараас хариу авч байна… (ойролцоогоор 1-2 минут)\n")

outputs = []
for i, prompt in enumerate(prompts):
    print(f"Prompt {i+1}/6 ажиллаж байна…")
    max_len = 400 if i == 5 else 180
    result = generator(prompt,
                       max_length=max_len,
                       num_return_sequences=1,
                       temperature=0.8,
                       do_sample=True,
                       truncation=True,
                       pad_token_id=50256)[0]["generated_text"]
    
    response = result[len(prompt):].strip()
    if response == "": response = result.strip()
    outputs.append(response)

print("\nБүх хариу авсан!\n")
print("="*100)

table = []
nltk_scores = []
sacre_scores = []

smoothie = SmoothingFunction().method4

for i in range(len(prompts)):
    # nltk BLEU
    ref_tokens = [references[i].split()]
    hyp_tokens = outputs[i].split()
    nltk_score = sentence_bleu(ref_tokens, hyp_tokens, smoothing_function=smoothie)
    nltk_scores.append(nltk_score)
    
    # sacreBLEU
    sacre_score = sacrebleu.sentence_bleu(outputs[i], [references[i]]).score
    sacre_scores.append(sacre_score)
    
    table.append([
        i+i+1,
        prompts[i][:70] + "…" if len(prompts[i]) > 70 else prompts[i],
        f"{nltk_score:.4f}",
        f"{sacre_score:.2f}"
    ])

#Print
print(tabulate(table,
               headers=["№", "Prompt (эхний хэсэг)", "nltk BLEU", "sacreBLEU"],
               tablefmt="github",
               stralign="left"))

print("\nДҮГНЭЛТ".center(100, "█"))
print(f"Хамгийн сайн prompt (sacreBLEU): #{sacre_scores.index(max(sacre_scores))+1} → {max(sacre_scores):.2f}")
print(f"Хамгийн муу  prompt (sacreBLEU): #{sacre_scores.index(min(sacre_scores))+1} → {min(sacre_scores):.2f}")