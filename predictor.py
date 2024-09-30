import torch
import cv2
import numpy as np
from joblib import load
import streamlit as st
# ... your existing code ...


# print(categories[pred])
def make_prediction(input_image):
  myModel = torch.load('DiseaseDetectionEpoch73.pth', map_location=torch.device('cpu'))

  

  #myModel.eval()  # Set model to evaluation mode #temp
  #st.write ("Model uploaded!") # You may remove this in your finalized web app!
  input_resized = cv2.resize(input_image, (128, 128))
  input_resized = np.swapaxes(input_resized, 0,2)
  input_resized = np.swapaxes(input_resized, 1,2)

  # Normalize the input image
  input_resized = input_resized / 255.0  # Normalize pixel values to [0, 1] #temp

    # Convert NumPy array to PyTorch tensor and move to the same device as the model
  input_tensor = torch.from_numpy(input_resized).float()  # Convert to float tensor
  input_tensor = input_tensor.to(next(myModel.parameters()).device)  # Move to model's device

  # Add a batch dimension (models usually expect batches of data)
  input_tensor = input_tensor.unsqueeze(0)

  # Now you can pass the tensor to the model
  pred = myModel(input_tensor)
  pred = np.argmax(pred.cpu().detach().numpy())
  # Output the predicted class
  #st.write(input_tensor)  # Check the preprocessed input tensor
  #st.write(f"Predicted class: {pred}")

  categories = ['Cashew anthracnose', 'Cashew gumosis', 'Cashew healthy',
  'Cashew leaf miner', 'Cashew red rust', 'Cassava bacterial blight',
  'Cassava brown spot', 'Cassava green mite', 'Cassava healthy',
  'Cassava mosaic', 'Maize fall armyworm', 'Maize grasshopper', 'Maize healthy',
  'Maize leaf beetle', 'Maize leaf blight', 'Maize leaf spot',
  'Maize streak virus', 'Tomato healthy', 'Tomato leaf blight',
  'Tomato leaf curl', 'Tomato septoria leaf spot', 'Tomato verticulium wilt',
  'fall army worm', 'healthy', 'herbicide burn', 'magnesium deficiency',
  'maize streak', 'multiple', 'nitrogen deficiency', 'potassium deficiency',
  'stalk borer', 'sulphur deficiency', 'zinc deficiency']

  st.cache_data.clear()
  return categories[pred]
