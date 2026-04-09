from flask import Flask,request,jsonify
app=Flask(__name__)
@app.route("/chat",methods=["POST"])
def chat():
    data=request.json.get("message","")
    return jsonify({"reply":f"3dvr assistant: {data}"})
@app.route("/health")
def health():
    return {"status":"ok"}
app.run(host="0.0.0.0",port=3000)
