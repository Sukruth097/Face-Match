from setuptools import setup

setup(
    name="src",
    version="0.0.1",
    author="Sukruth A V",
    description="A small package for Which Bollywood Celebrity You look like? Deep Learning Project",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    #url="https://github.com/Sukruth097/Face-Match",
    author_email="sukruthav007@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'mtcnn==0.1.0',
        'tensorflow==2.3.1',
        'keras==2.4.3',
        'keras-vggface==0.6',
        'keras_applications==1.0.8',
        'PyYAML',
        'tqdm',
        'scikit-learn',
        'streamlit',
        'bing-image-downloader'
    ]
)
