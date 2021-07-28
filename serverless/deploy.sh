# 将serverless服务需要的文件拷贝进serverless文件夹
echo "开始复制文件..."
cp user.json ./serverless
cp autoCheck.py ./serverless
cp requirements.txt ./serverless
cd ./serverless

# 开始安装依赖
echo "开始安装python脚本依赖..."
pip install --upgrade setuptools >/dev/null
pip install -r requirements.txt -t ./

# 开始部署到腾讯云
if [[ -z $TENCENT_SECRET_ID || -z $TENCENT_SECRET_KEY ]]; then
  echo "本地密钥授权错误,请检查密钥是否填写完整！"
  exit 1
else
  echo "开始安装Serverless Framework..."
  npm install -g serverless
  echo "开始部署..."
  sls deploy --debug
fi
