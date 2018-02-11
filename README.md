##PROBLEM STATEMENT
Crop Vandalism by animals, namely wild boar, nilgai, monkeys and other wild animals.
Animals visit the farms at time unknown. The unavailability of any patrolling, each  yaer causes around 30-35% of crop losses to the farmers.
High level fencing is too expensive and not durable.
Treck Location: Grambharti, Ahmedabad, Gujrat.

##INTRODUCTION
We present an Neural Network Solution to the above problem. The software uses image recognisation and convulation networks to detects the things its capturing live from an external capturing, here we have used a web camera patrolling the field using a rover. The precision can further be improved by using a 360 degree view camera.

###PRE-REQUISITES
#TENSORFLOW: GOOGLE DEEP LEARNING MODULE
#DARKFLOW
#DARKET


Apart from this we recommend a GPU based system(preferably NIVIDEA with CUDA installed) for smooth functioning of the project.

#TENSOR FLOW INSTALLATION
Follow the official documentation at: [here](https://www.tensorflow.org/install/)

#DARKFLOW INSTALLTION

Dependencies : Python3, tensorflow 1.0, numpy, opencv 3.

You can choose _one_ of the following three ways to get started with darkflow.

1. Just build the Cython extensions in place. NOTE: If installing this way you will have to use `./flow` in the cloned darkflow directory instead of `flow` as darkflow is not installed globally.
    ```
    python3 setup.py build_ext --inplace
    ```

2. Let pip install darkflow globally in dev mode (still globally accessible, but changes to the code immediately take effect)
    ```
    pip install -e .
    ```

3. Install with pip globally
    ```
    pip install .
    ```

4. Update

#DARKNET INSTALLTION

Dependencies : Python3, opencv 3.

Follow the steps to get started with darknet.

1. Clone the repository using the following command.
	```
	git clone https://github.com/pjreddie/darknet
	```

2. cd darknet

3. make

4. Update

Testing the model.

1. Get a pre-trained model using the following command.
	```
	wget https://pjreddie.com/media/files/yolo.weights
	```

2. Run the detector.
	```
	./darknet detect cfg/yolo.cfg yolo.weights data/dog.jpg
	```
	

###CONTRTIBUTORS

[SAI SIDDARTHA MARAM](https://github.com/siddu1998)		[TANUJ VISHNOI](https://github.com/vishnoitanuj)		[SACHIN PANDEY](https://github.com/sachin328)