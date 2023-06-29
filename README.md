THIS IS FOR EDUCATION PURPOSES ONLY
============

Ookla Speeedtest Salad Modification
-----
A simple Python script that overrides the workload definition for NDM to use your *real* Ookla Speedtest results instead of librespeed-cli. This is for **educational purposes only**.

Although not recommended as Salad will not be able to support you further, you can apply this modification by downloading the source code, and running the following codeblock below. It **will** ask for admin privelages as the Salad workload definition is in a protected folder.

```shell
python -m pip install -r requirements.txt
python main.py
```
### Notes
- It will ask for admin privelages
- It will store a backup of the original workload definition as `ndm_BACKUP.yaml` in your Salad workload definitions folder
- I am not responsible for any damage done using this
