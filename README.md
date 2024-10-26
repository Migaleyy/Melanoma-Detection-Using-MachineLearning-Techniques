# **Melanoma Detection Using Machine Learning Techniques**

## **Title of the Project**
**Melanoma Detection Using Machine Learning Techniques**



## **About**
Melanoma is a dangerous form of skin cancer that can be fatal if not detected early. Early detection and treatment can greatly improve patient outcomes. This project focuses on developing an automated system using machine learning to detect melanoma from dermatoscopic images. By utilizing deep learning models and image processing techniques, this tool aims to assist healthcare professionals in diagnosing melanoma more accurately and quickly.

The system uses state-of-the-art pre-trained models such as **AlexNet**, **ResNet50**, **VGG16**, and **VGG19** to classify skin lesions as either **melanoma** or **non-melanoma**. A user-friendly web interface allows dermatologists to upload lesion images and get diagnostic predictions with associated confidence scores.


## **Features**
- **Image Upload and Preprocessing:**
  - Users can upload dermatoscopic images, which are processed using techniques such as resizing, augmentation, and normalization.
  
- **Pre-trained Models for Classification:**
  - Leveraging well-known models like AlexNet, ResNet50, VGG16, and VGG19, the system delivers accurate melanoma predictions.
  
- **Prediction Interface:**
  - The web-based platform provides a simple, intuitive interface where users can receive prediction results.
  
- **Exploratory Data Analysis (EDA):**
  - The system allows for EDA to gain insights into the dataset, enabling better understanding of model performance and data distribution.
  
- **Cross-validation & Model Evaluation:**
  - The system evaluates model performance using metrics such as accuracy, precision, and recall, ensuring the robustness of the predictions.

- **Augmentation & Data Handling:**
  - The system uses the **Albumentation** library to enhance image quality and improve the model's ability to generalize on unseen data.



## **Requirements**
To successfully run this project, the following dependencies are required:

### **Programming Languages:**
- **Python 3.7+**

### **Libraries and Frameworks:**
- **TensorFlow or PyTorch**: For building and loading deep learning models.
- **Keras**: A high-level neural network API used for implementing the CNN models.
- **OpenCV**: For image loading, manipulation, and preprocessing.
- **Albumentations**: Used for augmenting images (rotation, flipping, contrast adjustments).
- **Scikit-learn**: For evaluation metrics like accuracy, precision, recall, and F1-score.
- **Flask/Django**: For creating a web-based interface where users can upload images and get predictions.
  
### **Pre-trained Models:**
- **AlexNet**
- **ResNet50**
- **VGG16**
- **VGG19**

### **Hardware:**
- **NVIDIA GPU (Recommended)**: For faster training and inference.
- **RAM**: At least 8 GB recommended for model loading and processing.



## **System Architecture**
The system is designed with a clear flow from image input to melanoma prediction. The architecture is divided into several key components:

### **1. Frontend (Web Interface)**
- A user-friendly web interface built using Flask or Django.
- Dermatologists and healthcare professionals can upload images and view diagnostic predictions.

### **2. Backend (Machine Learning Pipeline)**
- **ImageProcessor Class**:
  - Handles image loading and preprocessing tasks such as augmentation and normalization.
  - Files: `albumentation.ipynb`, `preaugmentation.ipynb`, `postaugmentation.ipynb`

- **ModelManager Class**:
  - Responsible for loading pre-trained models (AlexNet, ResNet50, VGG16, VGG19) and making predictions on preprocessed images.
  - Files: `pretrained.ipynb`, `final_notebook.ipynb`

- **ResultHandler Class**:
  - Displays prediction results, confidence scores, and evaluation metrics to the user.
  - File: `flutter.ipynb`

- **EDA Class**:
  - Performs exploratory data analysis to visualize data distribution and extract insights.
  - File: `EDA.ipynb`

### **3. Pre-trained Models**
The system uses pre-trained deep learning models for image classification:
- **AlexNet**
- **ResNet50**
- **VGG16**
- **VGG19**

Each of these models is fine-tuned on the skin lesion dataset to predict whether the lesion is melanoma or non-melanoma.


### **AlexNet**
![AlexNet-1](https://github.com/user-attachments/assets/e8d8697e-a34d-4c3c-8e85-f244ba478fb0)



### **Resnet50**
![resnet50](https://github.com/user-attachments/assets/e62135cf-7f6f-48ad-a578-977887133296)



### **Visual Geometry Group 16**
![vgg16_architecture](https://github.com/user-attachments/assets/7be74803-0b9b-4d9f-a7ef-edceca3e96f8)



### **Visual Geometry Group 19**
![vgg19_architecture](https://github.com/user-attachments/assets/a3db5561-5474-43f7-851e-377004495b99)

### **4. Flow of the System:**
1. **User uploads an image** via the frontend.
2. The **ImageProcessor** preprocesses the image (augmentation, resizing).
3. The **ModelManager** loads the pre-trained model and runs the prediction on the preprocessed image.
4. The **ResultHandler** displays the result, showing whether the lesion is melanoma or non-melanoma, along with a confidence score.
5. (Optional) The **EDA** module can be run to analyze data patterns and insights.

## **Output**

### **Home Page**
![Home_Page](https://github.com/user-attachments/assets/14bba206-8356-4a65-8593-9afa168b5164)

### **Result Page**
![Result_Page](https://github.com/user-attachments/assets/19a6102f-5add-4875-b302-c136e84b2e82)


## **Results and Impact**
- **Loss:** 0.18712055683135986
- **Accuracy:** 0.9338821172714233
- **Precision:** 0.9464677572250366
- **Recall:** 0.8421767354011536
- **ROC-AUC:** 0.951724112033844
- **PR-AUC:** 0.5401174426078796

### **VGG16-Based Convolutional Neural Networ**
![image](https://github.com/user-attachments/assets/a189f7a3-94b6-430e-9ecb-88dcaaacd5fe)
![image](https://github.com/user-attachments/assets/ec683518-503f-4f23-b020-ea86dbc98db5)

### **Simplified Convolutional Neural Network**
![image](https://github.com/user-attachments/assets/94445fcb-5880-46ad-924b-32c1bd57f182)
![image](https://github.com/user-attachments/assets/1a3bf631-07c2-47d6-9a01-7860d20783eb)

These metrics demonstrate that the system is highly effective in detecting melanoma from skin lesion images. The impact of this system is profound in healthcare settings, where early and accurate detection of melanoma is crucial for patient survival. This tool provides healthcare professionals with an additional layer of diagnostic support, reducing the time for diagnosis and improving accuracy.

### **Key Results:**
- Improved diagnosis speed by automating image analysis.
- Reduced subjectivity in diagnosis by using objective machine learning models.
- Higher detection rates for melanoma, helping healthcare providers make informed decisions.



## **Articles Published / References**
1. **ISIC Skin Cancer Dataset**: The International Skin Imaging Collaboration (ISIC) archive provided the dataset used for training and validation. [ISIC Archive](https://isic-archive.com)
2. **AlexNet**: Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton, "ImageNet Classification with Deep Convolutional Neural Networks", Advances in Neural Information Processing Systems, 2012.
3. **ResNet50**: He, Kaiming, et al. "Deep Residual Learning for Image Recognition", Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition, 2016.
4. **VGG16 & VGG19**: Simonyan, Karen, and Andrew Zisserman. "Very Deep Convolutional Networks for Large-Scale Image Recognition", arXiv preprint arXiv:1409.1556, 2014.
5. **Albumentations Library**: Open-source library used for image augmentation techniques. [Albumentations GitHub](https://github.com/albumentations-team/albumentations)
