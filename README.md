## *h*-index from the SAO/NASA Astrophysics Data System (ADS)

The package includes a Python code to automatically fetch [*h*-index](https://en.wikipedia.org/wiki/H-index) from the [SAO/NASA Astrophysics Data System (ADS)](https://ui.adsabs.harvard.edu) for a given [ORCID](https://orcid.org) (Open Researcher and Contributor ID), and an example PHP code (see below) on how to display the *h*-index on a webpage.

**IMPORTANT:** Please note that the latest *h*-index is automatically fetched from the ADS for all your publications linked to your ORCID. As such, it works correctly only if all your publications in the ADS have been linked (claimed) to your ORCID. See [here](https://ui.adsabs.harvard.edu/orcid-instructions/) on how to link your publications and ORCID in the ADS.

### Prepare the Python code

* Create an account at the [SAO/NASA Astrophysics Data System (ADS)](https://ui.adsabs.harvard.edu), if you do not already have one.
* Login into your ADS account.
* **Generate a new key** under [*Settings* > *API token*](https://ui.adsabs.harvard.edu/user/settings/token).
* Replace the **Your_ADS_API_Token** in line 21 of the Python code (compute_h_index.py) with your generated API key.
* Upload the Python code in to your server (i.e., where your other webpages are).

### Display *h*-index in your webpage

* If your webpage is in HTML, change the extension from `.html` to `.php` (i.e., change the file name from `name.html` to `name.php`)
* Create an [ORCID iD](https://orcid.org), if you do not have one.
* Add the following PHP code in where you want to display the *h*-index (in between your other HTML or PHP codes), and replace the **YOUR_ORCID_ID** with yours (only the number, e.g., `0000-0002-7711-5397`).
```
   <?php
     $orcid = YOUR_ORCID_ID
     $h_index = exec("python3 compute_h_index.py $orcid"); 
     $pid = intval(exec('python3 compute_h_index.py'));
     exec("kill $pid");
     echo $h_index;
   ?>
```
