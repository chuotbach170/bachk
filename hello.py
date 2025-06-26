@app.route("/submit", methods=["POST"])
def submit():
    code = request.form["code"]
    access = request.form["access"]

    # Mã truy cập do bạn định nghĩa
    if access != "123456":
        return "<h3 style='text-align:center;'>⛔ Sai mã truy cập</h3><p style='text-align:center;'><a href='/'>← Thử lại</a></p>"

    print(f"✅ Đã nhận mã: {code}")
    with open("ma_da_nhap.txt", "a", encoding="utf-8") as f:
        f.write(code + "\n")

    return render_template_string(f"""
    <!DOCTYPE html>
    <html><head><meta charset="utf-8"><title>OK</title>
    <style>body {{ display: flex; align-items: center; justify-content: center; height: 100vh; font-family: sans-serif; background: #f4f4f4; }}</style></head>
    <body><div style="text-align:center;"><h2>✅ Đã nhận mã: {code}</h2><a href="/">← Nhập tiếp</a></div></body></html>
    """)

