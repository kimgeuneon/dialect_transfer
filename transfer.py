from transformers import BartForConditionalGeneration, PreTrainedTokenizerFast

# 제주 방언 -> 표준어 모델 경로
jeju_model_path = "./kobart-finetuned-jeju3"
# 표준어 -> 경상도 방언 모델 경로
gyeongsang_model_path = "./kobart-finetuned-kyeongsang"

# 모델과 토크나이저 로드 (제주 방언 -> 표준어)
jeju_model = BartForConditionalGeneration.from_pretrained(jeju_model_path)
jeju_tokenizer = PreTrainedTokenizerFast.from_pretrained(jeju_model_path)

# 모델과 토크나이저 로드 (표준어 -> 경상도 방언)
gyeongsang_model = BartForConditionalGeneration.from_pretrained(gyeongsang_model_path)
gyeongsang_tokenizer = PreTrainedTokenizerFast.from_pretrained(gyeongsang_model_path)

# 테스트 입력 데이터 (제주 방언)
input_text_jeju = "서껑 허는 건 뭐 , 보리ᄊᆞᆯ에 ᄑᆞᆺ도 서끄곡 , 콩도 서끄곡 ."

# 입력 텍스트 출력
print("Input Text (Jeju Dialect):", input_text_jeju)

# 1단계: 제주 방언 -> 표준어 번역
input_ids_jeju = jeju_tokenizer.encode(input_text_jeju, return_tensors="pt")
output_ids_jeju = jeju_model.generate(input_ids_jeju, max_length=50, num_beams=4, early_stopping=True)
output_text_jeju = jeju_tokenizer.decode(output_ids_jeju[0], skip_special_tokens=True)

# 표준어 결과 출력
print("Standard Language:", output_text_jeju)

# 2단계: 표준어 -> 경상도 방언 번역
input_ids_standard = gyeongsang_tokenizer.encode(output_text_jeju, return_tensors="pt")
output_ids_gyeongsang = gyeongsang_model.generate(input_ids_standard, max_length=50, num_beams=4, early_stopping=True)
output_text_gyeongsang = gyeongsang_tokenizer.decode(output_ids_gyeongsang[0], skip_special_tokens=True)

# 경상도 방언 결과 출력
print("Gyeongsang Dialect:", output_text_gyeongsang)
