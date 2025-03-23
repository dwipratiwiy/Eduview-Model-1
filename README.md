#  Real-Time Object Detection for Student Cheating in a Classroom Using YOLO

![Detection in Clasroom](https://github.com/dwipratiwiy/Eduview-Model-1/blob/main/images/detection%20image.jpeg)

## Problem
Cheating in education, whether in exams or assignments, has become a major issue that undermines the quality of education in Indonesia. It prevents students from truly understanding the material and weakens both academic integrity and educational standards. According to reports from The Guardian and research by the International Center for Academic Integrity (ICAI), around 70% of students worldwide have engaged in academic dishonesty. Several factors contribute to this behavior, including lack of exam preparation, the desire to achieve high grades through dishonest means, inadequate supervision, and the inability of teachers or lecturers to detect cheating during exams. To address this issue, we have developed EduView, an AI-powered system that detects cheating behavior in real time within classrooms. This system aligns with SDG 4, which aims to ensure inclusive and equitable quality education and promote lifelong learning opportunities. Education quality is not only measured by infrastructure but also by strengthening human resources and fostering academic integrity.

## Workplan

![Detection in Clasroom](https://github.com/dwipratiwiy/Eduview-Model-1/blob/main/images/workplan.png)

## Dataset
Our dataset originates from Roboflow. We redistributed it into train (80%), validation (10%), and test (10%) sets. Augmentations include horizontal flip, brightness adjustment, and blur, with preprocessing resizing images to 640x640 pixels. The dataset contains six classes.
![dataset class](https://github.com/dwipratiwiy/Eduview-Model-1/blob/main/images/dataset%20split%20class.png)

## Training
The training process was conducted using four YOLO versions: YOLOv8, YOLOv9, YOLOv10, and YOLOv11, each trained for 30 epochs with a learning rate (LR) of 0.001 using the AdamW optimizer. A comparison was performed to determine the best YOLO version based on accuracy metrics, including mAP50, mAP50-95, precision, recall, and loss functions (classification loss and bounding box loss).
![perbandingan metriks](https://github.com/dwipratiwiy/Eduview-Model-1/blob/main/images/perbandingan%20matrik%20evaluasi.png)

## Result
From the comparison results, YOLOv8 was determined to be the best model. The evaluation and testing phases were then conducted using the test dataset.
![result](https://github.com/dwipratiwiy/Eduview-Model-1/blob/main/images/results.png)

## Deployment
The model was then saved in **.pt** format and deployed using **Reflex**.

## Team Members
| No | NIM | Name |
|----|-----------|-------------------------------|
| 1  | E1E122064 | La Ode Muhammad Yudhy Prayitno|
| 2  | E1E122010 | Dwi Pratiwi Aprilya Wahid     |
| 3  | E1E122099 | Icha Anawai                   |

## Reference
[Cheating Detection Through CCTV using YOLOv7](https://eprints.unram.ac.id/44273/2/Publikasi%20Ilmiah%20%282nd%20MIMSE%202023%29%20-%20Mizanul%20Ridho%20Aohana.pdf)

[Cheating Detection in Examinations Using Improved
YOLOv8 with Attention Mechanism](https://thescipub.com/pdf/jcssp.2024.1668.1680.pdf)


## License

[MIT](https://choosealicense.com/licenses/mit/)
