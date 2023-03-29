###### from previous setup.sh file #######

# create virtual environment
#python3 -m venv spacy_env

#activate virtual environment
#source ./spacy_env/bin/activate

# then install requirements
python3 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
python -m spacy download en_core_web_md


#### extras from requirements file

matplotlib
numpy
pandas
gensim
scikit-learn
spacy
tensorflow-cpu
bertopic
