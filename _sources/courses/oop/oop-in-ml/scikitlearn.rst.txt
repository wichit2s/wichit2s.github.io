`Scikit-Learn`
============================================================

Scikit-learn หรือ Sklearn เป็นชุดคำสั่งเสริมที่ใช้ภาษา Python เพื่อเป็นเครื่องมือช่วยสำหรับการประมวลผลข้อมูลและการเรียนรู้ของเครื่อง (machine learning) ทั้งในลักษณะของการจัดแบ่งข้อมูล (preprocessing), การเรียนรู้แบบมีผู้สอน (supervised learning), การเรียนรู้แบบไม่มีผู้สอน (unsupervised learning), และการประเมินผล (model evaluation) ดังนี้

การจัดแบ่งข้อมูล (Preprocessing):
------------------------------------------------------------

ชุดคำสั่งนี้อยู่ในหมวด `sklearn.model_selection <https://scikit-learn.org/stable/modules/classes.html#module-sklearn.model_selection>`_
ซึ่งมีคลาสที่ช่วยอำนวยความสะดวกในการสร้างชุดข้อมูลสำหรับการทดลองต่างได้แก่ KFold, LeaveOneOut, ShuffleSplit, StratifiedKFold, TimeSeriesSplit เป็นต้น

* `sklearn.model_selection.train_test_split() <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html#sklearn.model_selection.train_test_split>`_: ฟังก์ชันอำนวยความสะดวกในการแบ่งข้อมูลเป็นชุดฝึกและชุดทดสอบ

การแปลงข้อมูล

* `sklearn.preprocessing.StandardScaler() <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html#sklearn.preprocessing.StandardScaler>`_: ทำการปรับข้อมูลให้มี mean เท่ากับ 0 และ standard deviation เท่ากับ 1

* `sklearn.preprocessing.MinMaxScaler() <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html#sklearn.preprocessing.MinMaxScaler>`_: ทำการปรับข้อมูลให้อยู่ในช่วง [0, 1]

* `sklearn.preprocessing.OneHotEncoder() <https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html#sklearn.preprocessing.OneHotEncoder>`_: ทำการแปลงข้อมูล categorical เป็น binary vectors

การเรียนรู้แบบมีผู้สอน (Supervised Learning):
------------------------------------------------------------

Linear Models:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`sklearn.linear_model.LinearRegression() <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression>`_: สร้างโมเดล Linear Regression

`sklearn.linear_model.LogisticRegression() <https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html#sklearn.linear_model.LogisticRegression>`_: สร้างโมเดล Logistic Regression

Support Vector Machines (SVM):
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.svm.SVC() <https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html#sklearn.svm.SVC>`_: สร้างโมเดล Support Vector Classification

* `sklearn.svm.SVR() <https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVR.html#sklearn.svm.SVR>`_: สร้างโมเดล Support Vector Regression

Decision Trees:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.tree.DecisionTreeClassifier() <https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html#sklearn.tree.DecisionTreeClassifier>`_: สร้างโมเดล Decision Tree Classification

* `sklearn.tree.DecisionTreeRegressor() <https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html#sklearn.tree.DecisionTreeRegressor>`_: สร้างโมเดล Decision Tree Regression

Ensemble Methods:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.ensemble.RandomForestClassifier() <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html#sklearn.ensemble.RandomForestClassifier>`_: สร้างโมเดล Random Forest Classification

* `sklearn.ensemble.RandomForestRegressor() <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html#sklearn.ensemble.RandomForestRegressor>`_: สร้างโมเดล Random Forest Regression

* `sklearn.ensemble.GradientBoostingClassifier() <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html#sklearn.ensemble.GradientBoostingClassifier>`_: สร้างโมเดล Gradient Boosting Classification

การเรียนรู้แบบไม่มีผู้สอน (Unsupervised Learning):
------------------------------------------------------------

Clustering:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.cluster.KMeans() <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans>`_: สร้างโมเดล K-Means Clustering

* `sklearn.cluster.DBSCAN() <https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN>`_: สร้างโมเดล DBSCAN Clustering.

Dimensionality Reduction:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.decomposition.PCA() <https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA>`_: ทำ Principal Component Analysis เพื่อลดมิติของข้อมูล

การประเมินผล (Model Evaluation):
------------------------------------------------------------

* `sklearn.metrics.accuracy_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html#sklearn.metrics.accuracy_score>`_: คำนวณความแม่นยำของโมเดล

* `sklearn.metrics.precision_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.precision_score.html#sklearn.metrics.precision_score>`_, `sklearn.metrics.recall_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.recall_score.html#sklearn.metrics.recall_score>`_, `sklearn.metrics.f1_score() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score>`_: คำนวณ Precision, Recall, F1 Score

* `sklearn.metrics.confusion_matrix() <https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html#sklearn.metrics.confusion_matrix>`_: สร้าง Confusion Matrix

Cross-validation:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.model_selection.cross_val_score() <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.cross_val_score.html#sklearn.model_selection.cross_val_score>`_: ทำ Cross-validation เพื่อประเมินประสิทธิภาพของโมเดล

Hyperparameter Tuning:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.model_selection.GridSearchCV() <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.GridSearchCV.html#sklearn.model_selection.GridSearchCV>`_: ทำการค้นหา hyperparameter ที่ดีที่สุดจากชุดทดลอง

Pipeline:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.pipeline.Pipeline() <https://scikit-learn.org/stable/modules/generated/sklearn.pipeline.Pipeline.html#sklearn.pipeline.Pipeline>`_: สร้างลำดับขั้นตอนการประมวลผลข้อมูลที่สามารถใช้ได้ต่อเนื่อง

Feature Selection:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* `sklearn.feature_selection.SelectKBest() <https://scikit-learn.org/stable/modules/generated/sklearn.feature_selection.SelectKBest.html#sklearn.feature_selection.SelectKBest>`_: เลือกคุณลักษณะที่ดีที่สุดตามกลไกทางสถิติ

