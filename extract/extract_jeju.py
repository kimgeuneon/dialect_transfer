import os
import json

# JSON 파일들이 저장된 경로
json_folder_path = './1'  # JSON 파일이 저장된 폴더 경로
output_file_path = 'jeju_data.json'  # 최종 병합된 JSON 파일 이름

# JSON 파일 병합 및 변환 함수
def merge_and_transform_json(json_folder_path, output_file_path):
    merged_data = []  # 병합된 데이터를 담을 리스트

    # 폴더 내 JSON 파일 순회
    for filename in os.listdir(json_folder_path):
        if filename.endswith('.json'):  # JSON 파일만 처리
            file_path = os.path.join(json_folder_path, filename)

            try:
                # JSON 파일 열기
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    try:
                        data = json.load(json_file)  # JSON 파싱
                    except json.JSONDecodeError as e:   
                        print(f"JSON 파싱 오류: {file_path}, {e}")
                        continue  # JSON 파싱 오류가 발생하면 건너뜀

                    # "transcription" 키에서 데이터 변환
                    if isinstance(data.get('transcription'), dict):
                        transcription = data['transcription']
                        source = transcription.get('dialect', '')  # 기존 dialect를 source로 변환
                        target = transcription.get('standard', '')  # 기존 standard를 target으로 변환 

                        # 변환된 데이터를 리스트에 추가
                        merged_data.append({
                            "source": source,
                            "target": target
                        })
                    else:
                        print(f"유효하지 않은 데이터 구조: {file_path}")
            except Exception as e:
                print(f"파일 처리 중 오류 발생: {file_path}, {e}")

    # 병합된 데이터를 하나의 JSON 파일로 저장
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        json.dump(merged_data, output_file, ensure_ascii=False, indent=4)
        print(f"모든 JSON 데이터가 {output_file_path}에 병합 및 변환되었습니다.")

# JSON 병합 및 변환 실행
merge_and_transform_json(json_folder_path, output_file_path)
