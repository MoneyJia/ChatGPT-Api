import tiktoken

MODEL_NAME = "gpt-3.5-turbo-16k-0613"
encoder = tiktoken.encoding_for_model(MODEL_NAME)

def calculate_and_display_token_count(input_text:str):
    encoded_text = encoder.encode(input_text)
    token_count = len(encoded_text)
    
    print(f"输入的文本:'{input_text}'")
    print(f"对应的编码:{encoded_text}")
    print(f"Token数量: {token_count}")

calculate_and_display_token_count(input_text='测iToken大小')
