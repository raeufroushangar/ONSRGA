# Algorithm Description:

* **Input/Output:** algorithm takes a string of nucleic acid (e.g. reference genome) and returns a list of sequence reads according to the hypergeometric probability distribution (i.e. sampling  without replacement). 
* **Functionality:** algorithm breaks the string (input) into smaller fragments (output) that are within the desired input size (min, max). It will then add errors (substitutions or deletions) to each read to simulate Oxford Nanopore sequencing error rates per read.

<img width="2043" alt="Screen Shot 2020-12-15 at 7 57 17 AM" src="https://user-images.githubusercontent.com/39611565/202077013-ec38fb7f-afda-4cfe-955b-2bf43afe927c.png">


**Read generation process:**
<img width="2486" alt="Screenshot 2022-11-15 at 10 39 17 PM" src="https://user-images.githubusercontent.com/39611565/202077921-c178bcbd-88ef-4c24-850e-96fc53925521.png">

