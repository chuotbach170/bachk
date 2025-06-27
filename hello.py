from flask import Flask, request, send_file, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    code = request.form.get("code")
    access = request.form.get("access")

    if access != "123456":
        return render_template_string("""
          <h3 style="text-align:center;">⛔ Sai mã truy cập</h3>
          <p style="text-align:center;"><a href="/">← Thử lại</a></p>
        """)

    with open("ma_da_nhap.txt", "a", encoding="utf-8") as f:
        f.write(f"{code}\n")

    return render_template_string(f"""
      <!DOCTYPE html><html><head><meta charset="utf-8">
      <title>OK</title>
      <style>body{{display:flex;align-items:center;justify-content:center;
              height:100vh;font-family:sans-serif;background:#f4f4f4;}}
      </style></head><body>
        <div style="text-align:center;">
          <h2>✅ Đã nhận mã: {code}</h2>
          <a href="/">← Nhập tiếp</a>
        </div>
      </body></html>
    """)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

