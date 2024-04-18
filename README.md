# Stable Diffusion 모델 사용 가이드

Stable Diffusion은 Stability AI 및 Runway와의 협력을 통해 개발된 텍스트-이미지 변환 라텐트 확산 모델입니다. 이 모델은 512x512 이미지 해상도로 LAION-5B 데이터베이스의 하위 집합에 대해 훈련되었습니다.

## 시작하기 전에

본 모델을 사용하기 위해서는 먼저 적절한 conda 환경을 설정해야 합니다:

```bash
conda env create -f environment.yaml
conda activate ldm

conda install pytorch torchvision -c pytorch
pip install transformers==4.19.2 diffusers invisible-watermark
pip install -e .

mkdir -p models/ldm/stable-diffusion-v1/
ln -s <path/to/your/model.ckpt> models/ldm/stable-diffusion-v1/model.ckpt

python scripts/txt2img.py --prompt "a photograph of an astronaut riding a horse" --plms

python scripts/img2img.py --prompt "A fantasy landscape, trending on artstation" --init-img <path/to/your/sketch.jpg> --strength 0.8
