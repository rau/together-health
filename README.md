# TogetherHealth

## Installation Instructions

### Getting the code (this step requires git, which can be downloaded and installed online at [this link.](https://git-scm.com/downloads))

Open a folder on your local machine where you would like the files to be installed. Make sure this directory is empty.
Then navigate to the directory in your terminal using
```
cd [PATH TO DIRECTORY HERE]
```
After this, run:
```
git clone https://github.com/rau/together-health.git
```

All of the relevant files should now be on your computer! Congratulations. Following the rest of the steps will allow you to use the web app.

### Other Dependencies

First, install Python 3.7 or above from [this link.](https://www.python.org/downloads/)

The following Python packages must be installed.

```
blas                      1.0                         mkl  
brotli                    1.0.9                hb1e8313_2  
ca-certificates           2020.10.14                    0
certifi                   2021.10.8        py39hecd8cb5_0  
click                     7.1.2                      py_0  
cycler                    0.11.0             pyhd3eb1b0_0  
flask                     1.1.2                      py_0    
fonttools                 4.25.0             pyhd3eb1b0_0  
freetype                  2.11.0               hd8bbffd_0  
giflib                    5.2.1                haf1e3a3_0  
intel-openmp              2021.4.0          hecd8cb5_3538  
itsdangerous              1.1.0                      py_0    
jinja2                    2.11.2                     py_0    
jpeg                      9d                   h9ed2024_0  
kiwisolver                1.3.1            py39h23ab428_0  
lcms2                     2.12                 hf1fd2bf_0  
libcxx                    12.0.0               h2f01273_0  
libffi                    3.3                  hb1e8313_2  
libpng                    1.6.37               ha441bb4_0  
libtiff                   4.2.0                h87d7836_0  
libwebp                   1.2.0                hacca55c_0  
libwebp-base              1.2.0                h9ed2024_0  
lz4-c                     1.9.3                h23ab428_1  
markupsafe                2.0.1            py39h9ed2024_0  
matplotlib                3.5.0            py39hecd8cb5_0  
matplotlib-base           3.5.0            py39h4f681db_0  
mkl                       2021.4.0           hecd8cb5_637  
mkl-service               2.4.0            py39h9ed2024_0  
mkl_fft                   1.3.1            py39h4ab4a9b_0  
mkl_random                1.2.2            py39hb2f4e1b_0  
munkres                   1.1.4                      py_0  
ncurses                   6.3                  hca72f7f_2  
numpy                     1.21.2           py39h4b4dc7a_0  
numpy-base                1.21.2           py39he0bd621_0  
olefile                   0.46               pyhd3eb1b0_0  
openssl                   1.1.1l               h9ed2024_0  
packaging                 21.3               pyhd3eb1b0_0  
pillow                    8.4.0            py39h98e4679_0  
pip                       21.2.4           py39hecd8cb5_0  
pyparsing                 3.0.4              pyhd3eb1b0_0  
python                    3.9.7                h88f2d9e_1  
python-dateutil           2.8.2              pyhd3eb1b0_0  
readline                  8.1                  h9ed2024_0  
setuptools                58.0.4           py39hecd8cb5_0  
six                       1.16.0             pyhd3eb1b0_0  
sqlite                    3.36.0               hce871da_0  
tk                        8.6.11               h7bc2e8c_0  
tornado                   6.1              py39h9ed2024_0  
tzdata                    2021e                hda174b7_0  
werkzeug                  1.0.1                      py_0    
wheel                     0.37.0             pyhd3eb1b0_1  
xz                        5.2.5                h1de35cc_0  
zlib                      1.2.11               h1de35cc_3  
zstd                      1.4.9                h322a384_0  
```

This extensive list can usually be acquired by running the following installations in succession:

```
pip install sqlite3
pip install flask
```

Now, you should be good to try and run the web app!

### Running the web application

Create a file named '.env' with the following info:

```
export SECRET_KEY=[INSERT YOUR OWN CUSTOMLY CREATED SECRET KEY]
export FLASK_DEBUG=True
export FLASK_APP=run.py
```

In order for the full site to work on a computer locally as intended there are a few other dependencies.
 
# Once the website is up and running as expected... 
 
## Logging In

The website has a register page, where users can register with their name, a username, and a password.

Register for an account, and login using the account information.

## Receiving recommendations

Navigate to the "My Form" page in order to enter your criteria for a healthcare plan. The site will store these preferences and then identify 5 plans that are best suited for that set of preferences, which will be displayed on the "My Plan" page.

## About

The about page details the purpose of the site, but also come implementation details specific to this project submission.



