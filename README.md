# 충북대학교 제조 AI 실제 (8884023-01) - 7주차 실습 및 과제

- **작성자**: 2026154001 정용석
- **주제**: CNN 기초, 고전 CNN 아키텍처, 전이학습·미세조정

## 노트북

| 번호 | 노트북 | 내용 | 실측 결과 (단일 1회 실행) |
|:---:|:---|:---|:---|
| Lab 7-1 | [Lab7_1.cnn_mnist_convolution_pooling.ipynb](./2026154001_정용석_Lab7_1.cnn_mnist_convolution_pooling.ipynb) | 합성곱·풀링 파라미터 실험, MNIST 간단 CNN | MNIST 테스트 정확도 98.43% (3 epochs) |
| Lab 7-2 | [Lab7_2.classic_cnn.ipynb](./2026154001_정용석_Lab7_2.classic_cnn.ipynb) | LeNet-5 학습, VGG16 추론, 구조·복잡도 비교 | LeNet-5 MNIST 테스트 정확도 98.11% (5 epochs) |
| Lab 7-3 | [Lab7_3.inception_resnet_finetuning_transfer.ipynb](./2026154001_정용석_Lab7_3.inception_resnet_finetuning_transfer.ipynb) | InceptionV3 미세조정, ResNet50 기반 CIFAR-10 전이학습 | CIFAR-10 테스트 정확도 25.63% (3 epochs) |

## 결과 해석 및 공시

- **Lab 7-3의 25.63%는 낮은(LOW) 베이스라인입니다.** 224x224 사전학습 ResNet50에 32x32 CIFAR-10 이미지를 입력하고 가중치를 동결한 채 3 epochs만 학습한 결과이며, 성공적인 전이학습 성능으로 주장하지 않습니다. 전이학습 파이프라인 구현 실습 결과로 해석해야 합니다.
- **모든 수치는 단일 1회 실행 결과**이며 반복 실행으로 검증하지 않았습니다.
- **코끼리 이미지 출처**: 원본 Googleapis URL이 403 Forbidden(AccessDenied)을 반환하여, 외부 Hackaday 호스팅 이미지(`https://cdn.hackaday.io/images/1219231493836853483.jpg`, 15,881 bytes, SHA256 `930f108d6d8487216ee8e6c8ea35ca5679caad58ba4e4e948c4ae80ab5c3ef27`)로 대체했습니다. 출처가 검증되지 않은 외부 이미지이며 Keras 등 특정 기관의 보증을 의미하지 않습니다.
- **커널 정보**: 노트북 메타데이터에는 강의 배포 원본 규격인 `icp2026` (`python3`)가 저장되어 있으나, 실제 실행은 격리 가상환경 커널(`lms-tg11308`; Python 3.12, TensorFlow 2.21, Keras 3.15)에서 이루어졌습니다.
- 노트북 파일은 실행 완료본 그대로이며 업로드 과정에서 내용을 수정하지 않았습니다.
