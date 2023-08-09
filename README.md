# h-index from SAO/NASA Astrophysics Data System (ADS)

The package includes a Python code to automatically fetch h-index from SAO/NASA Astrophysics Data System (ADS) for a given ORCID (Open Researcher and Contributor ID), and an exmaple PHP code (see below) on how to display the h-index on a webpage.

## Prepare the Python code
* Creat an account at the <a href="https://ui.adsabs.harvard.edu" target="_blank">SAO/NASA Astrophysics Data System (ADS)</a>, if you do not already have one.
* Login into your ADS account.
* **Generate a new key** under [*Settings* -> *API token*](https://ui.adsabs.harvard.edu/user/settings/token).
* Replace the **Your_ADS_API_Token** in line 21 of the Python code (compute_h_index.py).
* Upload the Python code to your server (i.e., where your other webpages are).

## Display h-index in your webpage
* If your webpage is in HTML, change the extension from `.html` to `.php` (i.e., change the file name from `name.html` to `name.php`)
* Create an [ORCID iD](https://orcid.org), if you do not have one.
* Add the following PHP code in where you want to display the h-index (in between your other HTML or PHP codes), and replace the **YOUR_ORCID_ID** with yours (only the ID number, e.g., `0000-0002-7711-5397`).
```
   <?php
     $orcid = YOUR_ORCID_ID
     $h_index = exec("python3 compute_h_index.py $orcid"); 
     $pid = intval(exec('python3 compute_h_index.py'));
     exec("kill $pid");
     echo $h_index;
   ?>
```
