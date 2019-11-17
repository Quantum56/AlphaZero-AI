from setuptools import setup

setup(
   name='AlphaZero-AI',
   version='1.0',
   description='Modular AI using AlphaZero neural networking',
   author='Quantum56',
   packages=['AlphaZero-AI'],  #same as name
   package_dir={'AlphaZero-AI': 'src\\DeepReinforcementLearning'},
   install_requires=['absl-py','appnope','astor','bleach','cycler','decorator','graphviz','grpcio','h5py','html5lib','ipython','ipython-genutils','jedi','jupyter-client','jupyter-core','Keras',
   'kiwisolver','Markdown','matplotlib','numpy','parso','pexpect','pickleshare','prompt-toolkit','protobuf','ptyprocess','pydot','pydot-ng','Pygments','pyparsing','python-dateutil',
   'pytz','PyYAML','pyzmq','scipy','simplegeneric','six','tensorboard','tensorflow','termcolor','tornado','traitlets','wcwidth','Werkzeug'], #external packages as dependencies
)