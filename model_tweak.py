import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.utils.np_utils import to_categorical
from keras.layers import Dense
from keras.optimizers import Adam
from keras.backend import clear_session
def model_train(neurons , model , epochs , test) : 
	model.add(Dense(units = neurons , input_dim = 28*28 , activation = 'relu'))
	model.add(Dense(units=200 , input_dim = 28*28 , activation = 'relu'))
	model.add(Dense(units=60 , input_dim = 28*28 , activation = 'relu'))
	model.add(Dense(units=10 , input_dim = 28*28 , activation = 'softmax'))
	model.compile( optimizer= "Adam" , loss='categorical_crossentropy', 
	             metrics=['accuracy'] )
	return model
def validate(fit_model, epochs):
	acc = fit_model.history
	accuracy = acc['accuracy'][epochs-1] * 100
	accuracy = int(accuracy)
	f= open("modelaccuracy.txt","w+")
	f.write(str(accuracy))
	f.close()
	print(" Now after iteration Accuracy : " , accuracy ,"%")
	return accuracy
(train_X , train_y), (test_X , test_y) = mnist.load_data("mymnist.data")
test_X = test_X.reshape(-1 , 28*28)
train_X = train_X.reshape(-1 ,  28*28)
test_X = test_X.astype("float32")
train_X = train_X.astype("float32")
test_y = to_categorical(test_y)
train_y = to_categorical(train_y)
neurons = 10
accuracy = 0
epochs = 1
test = 1
trigger = 0
while int(accuracy) < 90 :
	if trigger == 1 :
		model = keras.backend.clear_session()
		neurons = neurons+10
		epochs = epochs+1 
		test = test + 1
	model = Sequential()
	model = model_train(neurons , model , epochs , test)
	fit = model.fit(train_X ,  train_y , epochs = epochs , verbose =  False)
	accuracy=validate(fit , epochs)
	trigger = 1
