import os

# 1. 自动定位当前脚本所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. 拼出完整的 res 路径 (增加容错)
res_path = os.path.join(current_dir, "app", "src", "main", "res")

# 检查 res 目录是否存在，不存在说明你还没建 res 文件夹
if not os.path.exists(res_path):
    print(f"❌ 错误：找不到路径 {res_path}")
    print("请检查你是否有 'app/src/main/res' 这个层级！")
else:
    res_data = {
        "values": {"app_name": "Base64 Pro", "input_hint": "Enter text or Base64...", "btn_encode": "🔒 Encode", "btn_decode": "🔓 Decode", "btn_clear": "Clear", "error_msg": "❌ Invalid Base64!"},
        "values-zh-rCN": {"app_name": "Base64加解密", "input_hint": "在此输入文本或Base64...", "btn_encode": "🔒 编码", "btn_decode": "🔓 解码", "btn_clear": "清空", "error_msg": "❌ 格式错误！"},
        "values-es": {"app_name": "Base64 Pro", "input_hint": "Ingrese texto...", "btn_encode": "🔒 Codificar", "btn_decode": "🔓 Decodificar", "btn_clear": "Limpiar", "error_msg": "❌ Error!"},
        "values-pt": {"app_name": "Base64 Pro", "input_hint": "Insira o texto...", "btn_encode": "🔒 Codificar", "btn_decode": "🔓 Decodificar", "btn_clear": "Limpar", "error_msg": "❌ Erro!"},
        "values-ja": {"app_name": "Base64変換", "input_hint": "テキストを入力...", "btn_encode": "🔒 エンコード", "btn_decode": "🔓 デコード", "btn_clear": "クリア", "error_msg": "❌ エラー！"},
        "values-de": {"app_name": "Base64 Konverter", "input_hint": "Text eingeben...", "btn_encode": "🔒 Codieren", "btn_decode": "🔓 Decodieren", "btn_clear": "Löschen", "error_msg": "❌ Fehler!"}
    }

    for folder, content in res_data.items():
        path = os.path.join(res_path, folder)
        os.makedirs(path, exist_ok=True)
        xml = ['<?xml version="1.0" encoding="utf-8"?>', '<resources>']
        for k, v in content.items(): xml.append(f'    <string name="{k}">{v}</string>')
        xml.append('</resources>')
        with open(os.path.join(path, "strings.xml"), "w", encoding="utf-8") as f:
            f.write("\n".join(xml))
    
    print(f"✅ 成功！已在 {res_path} 下生成 6 国语言包。")