from flask import Flask, render_template, request

app = Flask(__name__) 


def check_url(url):
    warnings = []
    url = url.strip().lower()

    if not url.startswith("https://"):
        warnings.append("URL does not use HTTPS")

    if "@" in url:
        warnings.append("URL contains an @ symbol")

    if "xn--" in url:
        warnings.append("URL contains an encoded domain name")

    if len(url) > 100:
        warnings.append("URL is unusually long")

    if warnings:
        return warnings

    return []


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    url = ""

    if request.method == "POST":
        url = request.form.get("url", "").strip()

        if url:
            warnings = check_url(url)

            if warnings:
                result = {
                    "status": "Suspicious signs detected",
                    "warnings": warnings
                }
            else:
                result = {
                    "status": "No suspicious signs found",
                    "warnings": []
                }

    return render_template(
        "index.html",
        result=result,
        url=url
    )


if __name__ == "__main__":
    app.run(debug=True)