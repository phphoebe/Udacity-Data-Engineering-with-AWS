# PySpark Installation

* install Java using [Homebrew](https://formulae.brew.sh/formula/openjdk@11)

  ```
  brew install openjdk@11
  ```
* for the system Java wrappers to find this JDK, symlink it with
  ```
  sudo ln -sfn $HOMEBREW_PREFIX/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
  ```
  
* create a virtual environment
  ```
  python3 -m venv spark-test
  ```

* activate the virtual env
  ```
  source spark-test/bin/activate
  ```
  
* install PySpark & other useful packages
  ```
  pip install pyspark
  pip install mrjob
  pip install numpy
  pip install pandas
  pip install matplotlib
  ```
  
## Setup PySpark and Jupyter Notebook

* install in the `spark-test` virtual env
  ```
  pip install jupyterlab
  pip install ipykernel
  ```
  
* register the new virtual env with Jupyter so that you can use it within JupyterLab
  ```
  python3 -m ipykernel install --user --name='spark-test'
  ```
  
Now open an existing/create a new `.ipynb` file in VS Code and select the `spark-test` Kernel to use
