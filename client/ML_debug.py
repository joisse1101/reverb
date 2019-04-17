<tempfile.SpooledTemporaryFile instance at 0x6284c0a8>
('Error encountered while parsing file: ', <type 'file'>)
Traceback (most recent call last):
  File "jasper.py", line 157, in <module>
    app.run()
  File "jasper.py", line 126, in run
    conversation.handleForever()
  File "/home/pi/reverb/client/conversation.py", line 52, in handleForever
    input = self.mic.activeListenToAllOptions(threshold)
  File "/home/pi/reverb/client/mic.py", line 261, in activeListenToAllOptions
    detector.print_prediction(f)
  File "/home/pi/reverb/client/CarHorn_Detector.py", line 41, in print_prediction
    predicted_vector = model.predict_classes(prediction_feature)
  File "/usr/local/lib/python2.7/dist-packages/keras/engine/sequential.py", line 267, in predict_classes
    proba = self.predict(x, batch_size=batch_size, verbose=verbose)
  File "/usr/local/lib/python2.7/dist-packages/keras/engine/training.py", line 1149, in predict
    x, _, _ = self._standardize_user_data(x)
  File "/usr/local/lib/python2.7/dist-packages/keras/engine/training.py", line 751, in _standardize_user_data
    exception_prefix='input')
  File "/usr/local/lib/python2.7/dist-packages/keras/engine/training_utils.py", line 92, in standardize_input_data
    data = [standardize_single_array(x) for x in data]
  File "/usr/local/lib/python2.7/dist-packages/keras/engine/training_utils.py", line 27, in standardize_single_array
    elif x.ndim == 1:
AttributeError: 'tuple' object has no attribute 'ndim'
