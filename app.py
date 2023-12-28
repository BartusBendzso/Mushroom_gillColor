import streamlit as st
import pandas as pd
import numpy as np
from prediction import predict
import sklearn

st.title('Classifying Mushrooms')
st.markdown('Predicting Mushrooms Gill-color')

col1, col2 = st.columns(2)

cap_shape_list = ['convex', 'bell', 'sunken', 'flat', 'knobbed', 'conical']

cap_color_list = ['brown', 'yellow', 'white', 'gray', 'red', 'pink', 'buff','purple', 'cinnamon', 'green']

odor_list = ['pungent', 'almond', 'anise', 'none', 'foul', 'creosote', 'fishy','spicy', 'musty']

gill_attachment_list = ['free', 'attached']

class_list = ['Poisonous', 'Edible']

stalk_shape_list = ['enlarging', 'tapering']

stalk_root_list = ['equal', 'club', 'bulbous', 'rooted', 'missing']

stalk_surface_above_ring_list = ['smooth', 'fibrous', 'silky', 'scaly']

stalk_surface_below_ring_list = ['smooth', 'fibrous', 'scaly', 'silky']

stalk_color_above_ring_list = ['white', 'gray', 'pink', 'brown', 'buff', 'red', 'orange','cinnamon', 'yellow']

stalk_color_below_ring_list = ['white', 'pink', 'gray', 'buff', 'brown', 'red', 'yellow','orange', 'cinnamon']

ring_type_list = ['pendant', 'evanescent', 'large', 'flaring', 'none']

spore_print_color_list = ['black', 'brown', 'Purple', 'chocolate', 'White', 'green', 'Orange', 'Yellow', 'buff']

population_list = ['scattered', 'numerous', 'abundant', 'several', 'solitary','clustered']


with col1:
    st.text("Mushroom Features")
    
    cap_shape_input = st.selectbox(
        'Select cap-shape',
        ('convex', 'bell', 'sunken', 'flat', 'knobbed', 'conical'))
    st.write('You selected:', cap_shape_input)
    
    cap_color_input = st.selectbox(
        'Select cap-color',
        ('brown', 'yellow', 'white', 'gray', 'red', 'pink', 'buff','purple', 'cinnamon', 'green'))
    st.write('You selected:', cap_color_input)
    
    odor_input = st.selectbox(
        'Select odor',
        ('pungent', 'almond', 'anise', 'none', 'foul', 'creosote', 'fishy','spicy', 'musty'))
    st.write('You selected:', odor_input)
    
    gill_attachment_input = st.selectbox(
        'Select gill-attachment',
        ('free', 'attached'))
    st.write('You selected:', gill_attachment_input)
    
    class_input = st.selectbox(
        'Select class',
        ('Poisonous', 'Edible'))
    st.write('You selected:', class_input)
    
    stalk_shape_input = st.selectbox(
        'Select stalk-shape',
        ('enlarging', 'tapering'))
    st.write('You selected:', stalk_shape_input)
    
    stalk_root_input = st.selectbox(
        'Select stalk-root',
        ('equal', 'club', 'bulbous', 'rooted', 'missing'))
    st.write('You selected:', stalk_root_input)
    
    stalk_surface_above_ring_input = st.selectbox(
        'Select stalk-surface-above-ring',
        ('smooth', 'fibrous', 'silky', 'scaly'))
    st.write('You selected:', stalk_surface_above_ring_input)
    
    stalk_surface_below_ring_input = st.selectbox(
        'Select stalk-surface-below-ring',
        ('smooth', 'fibrous', 'scaly', 'silky'))
    st.write('You selected:', stalk_surface_below_ring_input)
    
    stalk_color_above_ring_input = st.selectbox(
        'Select stalk-color-above-ring',
        ('white', 'gray', 'pink', 'brown', 'buff', 'red', 'orange','cinnamon', 'yellow'))
    st.write('You selected:', stalk_color_above_ring_input)
    
    stalk_color_below_ring_input = st.selectbox(
        'Select stalk-color-below-ring',
        ('white', 'pink', 'gray', 'buff', 'brown', 'red', 'yellow','orange', 'cinnamon'))
    st.write('You selected:', stalk_color_below_ring_input)
    
    ring_type_input = st.selectbox(
        'Select ring-type',
        ('pendant', 'evanescent', 'large', 'flaring', 'none'))
    st.write('You selected:', ring_type_input)
    
    spore_print_color_input = st.selectbox(
        'Select spore-print-color',
        ('black', 'brown', 'Purple', 'chocolate', 'White', 'green', 'Orange', 'Yellow', 'buff'))
    st.write('You selected:', spore_print_color_input)
    
    population_input = st.selectbox(
        'Select population',
        ('scattered', 'numerous', 'abundant', 'several', 'solitary','clustered'))
    st.write('You selected:', population_input)
    

cap_shape_array = np.array([2, 0, 5, 3, 4, 1])
cap_shape = cap_shape_array[cap_shape_list.index(cap_shape_input)]

cap_color_array = np.array([0, 9, 8, 3, 7, 5, 1, 6, 2, 4])
cap_color = cap_color_array[cap_color_list.index(cap_color_input)]

odor_array = np.array([7, 0, 1, 6, 4, 2, 3, 8, 5])
odor = odor_array[odor_list.index(odor_input)]

gill_attachment_array = np.array([1, 0])
gill_attachment = gill_attachment_array[gill_attachment_list.index(gill_attachment_input)]

class_array = np.array([1, 0])
class_ = class_array[class_list.index(class_input)]

stalk_shape_array = np.array([0, 1])
stalk_shape = stalk_shape_array[stalk_shape_list.index(stalk_shape_input)]

stalk_root_array = np.array([2, 1, 0, 4, 3])
stalk_root = stalk_root_array[stalk_root_list.index(stalk_root_input)]

stalk_surface_above_ring_array = np.array([3, 0, 2, 1])
stalk_surface_above_ring = stalk_surface_above_ring_array[stalk_surface_above_ring_list.index(stalk_surface_above_ring_input)]

stalk_surface_below_ring_array = np.array([3, 0, 1, 2])
stalk_surface_below_ring = stalk_surface_below_ring_array[stalk_surface_below_ring_list.index(stalk_surface_below_ring_input)]

stalk_color_above_ring_array = np.array([7, 3, 5, 0, 1, 6, 2, 4, 8])
stalk_color_above_ring = stalk_color_above_ring_array[stalk_color_above_ring_list.index(stalk_color_above_ring_input)]

stalk_color_below_ring_array = np.array([7, 5, 3, 1, 0, 8, 6, 2, 4])
stalk_color_below_ring = stalk_color_below_ring_array[stalk_color_below_ring_list.index(stalk_color_below_ring_input)]

ring_type_array = np.array([4, 0, 2, 1, 3])
ring_type = ring_type_array[ring_type_list.index(ring_type_input)]

spore_print_color_array = np.array([4, 5, 1, 7, 2, 8, 3, 0, 6])
spore_print_color = spore_print_color_array[spore_print_color_list.index(spore_print_color_input)]

population_array = np.array([3, 2, 0, 4, 5, 1])
population = population_array[population_list.index(population_input)]


# cap_shape, cap_color, odor, gill_attachment, class_, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, ring_type, spore_print_color, population

model_list = ['gill_color_classifier_DTree_model.pkl', 'gill_color_classifier_LR_model.pkl', 'gill_color_classifier_RF_model.pkl', 'gill_color_classifier_SVM_model.pkl']
model_label = ['Decision Tree', 'Logistic Regression', 'Random Forest', 'SVM']

with col2:
    model_input = st.selectbox(
        'Select model',
        ('Decision Tree', 'Logistic Regression', 'Random Forest', 'SVM'))
    st.write('You selected:', model_input)
    
    if st.button("Predict type of Gill-color"):
        result = predict(
            np.array([[cap_shape, cap_color, odor, gill_attachment, class_, stalk_shape, stalk_root, stalk_surface_above_ring, stalk_surface_below_ring, stalk_color_above_ring, stalk_color_below_ring, ring_type, spore_print_color, population]]), model_list[model_label.index(model_input)])
        st.text(str(result[0]))
