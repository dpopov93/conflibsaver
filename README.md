# conflibsaver
Library for easy working with configuration files

[![License GPL](https://img.shields.io/badge/license-GPL-blue.svg)](LICENSE)

### Lib functions 🔧
| Name                | Arguments               | Description                                                     | Return type    |
| ------------------- | ----------------------- | --------------------------------------------------------------- | -------------- |
| read_file           |                         | Reads file, recording to self.data_string                       | Boolean        |
| create_file         |                         | Create configuration file                                       | Boolean        |
| create_path_to_file |                         | Create path to file                                             | Boolean        |
| install_file_path   | conf_file_path          | Validate and saves to configuration file name and path of file  | String         |
| param_count         |                         | Return count of parameters in config file                       | Integer        |
| set_param           | param_name, param_value | Set parameter value by name                                     | Boolean        |
| get_param           | param_name              | Return value of parameter by name                               | String or None |
| has_param           | param_name              | Check for an existing parameter                                 | Boolean        |
| save_data           |                         | Saves data to file                                              | Boolean        |
| data_to_string      |                         | Converts data in one line (syntax conflib file)                 | String         |
| get_filename        |                         | Returns name of config file                                     | String         |
| get_path            |                         | Returns path of config file                                     | Boolean        |
| dbg                 | text                    | Display output of errors if display messages is on              |                |

### Thank You!
Please ⭐️ this repo and share it with others

### Syntax 🔌
For include library to your project you need to import lib:

       from conflibsaver import conflibsaver
Create settings instance:

       settings = conflibsaver("~/.config/myapplication/settings.cfg")
Create or rewrite parameter "param1" with value "some_value":

       settings.set_param("param1", "some_value")
Get value of parameter "param1":

       if settings.has_param("param1"):
           print(settings.get_param("param1"))
To get count of parameters use param_count():

       print(settings.param_count())
Printing name of file and path of filename:

       print("file:", settings.get_filename())
       print("dir:", settings.get_path())
Data save when you close the application, but you may get this manually:

       settings.save_data()

### Attention
* Please don't use in parameter names or value whitespaces or special symbol '='

### Contributing 💡
If you want to contribute to this project and make it better with new ideas, your pull request is very welcomed.
If you find any issue just put it in the repository issue section, thank you.
