
<ul class="inline_list">
    <li><a href="#bioc-version">Using Bioconductor</a></li>
	<li><a href="#install-R">Install&nbsp;R</a></li>
	<li><a href="#install-bioconductor-packages">Install&nbsp;Packages</a></li>
	<li><a href="#find-bioconductor-packages">Find&nbsp;Packages</a></li>
	<li><a href="#update-bioconductor-packages">Update&nbsp;Packages</a></li>
	<li><a href="#troubleshoot-bioconductor-packages">Troubleshoot&nbsp;Package&nbsp;Installations</a></li>
	<li><a href="#why-biocLite">Why&nbsp;biocLite()?</a></li>
	<li><a href="#preconfigured">Pre-configured&nbsp;Bioconductor</a></li>
</ul>


<h2 id="bioc-version">Using <em>Bioconductor</em></h2>

The current release of _Bioconductor_ is version
<%=config[:release_version] %>; it works with R version
<%=config[:r_version_associated_with_release]%>. Users of older R and
_Bioconductor_ must update their installation to take advantage
of new features and to access packages that have been added to
_Bioconductor_ since the last release.

[Install](#install-R) the latest release of R, then get the latest version of
_Bioconductor_ by starting R and entering the commands

    ## try http:// if https:// URLs are not supported
    source("https://bioconductor.org/biocLite.R")
    biocLite()

Details, including instructions to
[install additional packages](#install-bioconductor-packages) and to
[update](#update-bioconductor-packages),
[find](#find-bioconductor-packages), and
[troubleshoot](#troubleshoot-bioconductor-packages) are provided
below.  A [devel](/developers/how-to/useDevel/) version of
_Bioconductor_ is available. There are good
[reasons for using `biocLite()`](#why-biocLite) for managing
_Bioconductor_ resources.

<h2 id="install-R">Install R</h2>

1. Download the most recent version of [R][].  The [R FAQs][] and the [R
Installation and Administration Manual][1] contain detailed instructions
for installing R on various platforms (Linux, OS X, and Windows being
the main ones).

[R]: http://www.r-project.org/
[R FAQs]: http://cran.r-project.org/faqs.html
[1]: http://cran.r-project.org/doc/manuals/R-admin.html

2. Start the R program; on Windows and OS X, this will usually mean
   double-clicking on the R application, on UNIX-like systems, type
   "R" at a shell prompt.

3. As a first step with R, start the R help browser by typing
   `help.start()` in the R command window. For help on any
   function, e.g. the "mean" function, type `? mean`.

<p class="back_to_top">[ <a href="#top">Back to top</a> ]</p>

<h2 id="install-bioconductor-packages">Install <em>Bioconductor</em> Packages</h2>

Use the `biocLite.R` script to install _Bioconductor_ packages. To
install core packages, type the following in an R command window:

    ## try http:// if https:// URLs are not supported
    source("https://bioconductor.org/biocLite.R")
    biocLite()

Install specific packages, e.g., "GenomicFeatures" and "AnnotationDbi", with

    biocLite(c("GenomicFeatures", "AnnotationDbi"))

The `biocLite()` function (in the BiocInstaller package installed by
the `biocLite.R` script) has arguments that change its default
behavior; type `?biocLite` for further help.

<p class="back_to_top">[ <a href="#top">Back to top</a> ]</p>

<h2 id="find-bioconductor-packages">Find <em>Bioconductor</em> Packages</h2>

Visit the [software package list](/packages/release/BiocViews.html#___Software)
to discover available packages.

<p class="back_to_top">[ <a href="#top">Back to top</a> ]</p>

<h2 id="update-bioconductor-packages">Update Installed <em>Bioconductor</em> Packages</h2>

_Bioconductor_ packages, especially those in the development branch, are
updated fairly regularly. To identify packages requiring update within
your version of _Bioconductor_, start a new session of R and enter

    ## try http:// if https:// URLs are not supported
    source("https://bioconductor.org/biocLite.R")
	biocLite()                  ## R version 3.0 or later

Use the argument `ask=FALSE` to update old packages without being
prompted.  For older versions of `R`, use the command
`biocLite(NULL)`.  Read the help page for `?biocLite` for additional
details.

<h3 id="upgrade-bioconductor-packages">Upgrading installed <em>Bioconductor</em> packages</h3>

Some versions of R support more than one version of _Bioconductor_. To
use the latest version of _Bioconductor_ for your version of R, enter

    ## try http:// if https:// URLs are not supported
    source("https://bioconductor.org/biocLite.R")
	biocLite("BiocUpgrade")     ## R version 2.15 or later

Read the help page for `?BiocUpgrade` for additional details. Remember
that more recent versions of _Bioconductor_ may be available if your
version of R is out-of-date.

For more detail on <em>Bioconductor</em> approaches to versioning, see
the <a
href="/help/newsletters/2016_January/#managing-package-versions-with-">newsletter</a>
and version numbering <a
href="/developers/how-to/version-numbering/">developer reference</a>.

<h3>Recompiling installed <em>Bioconductor</em> packages</h3>

Rarely, underlying changes in the operating system require ALL
installed packages to be recompiled for source (C or Fortran)
compatibility. One way to address this might be to start a new R
session and enter

    ## try http:// if https:// URLs are not supported
    source("https://bioconductor.org/biocLite.R")
    pkgs <- rownames(installed.packages())
    biocLite(pkgs, type="source")

As this will reinstall all currently installed packages, it likely
involves a significant amount of network bandwidth and compilation
time. All packages are implicitly updated, and the cumulative effect
might introduce wrinkles that disrupt your work flow. It also requires
that you have the necessary compilers installed.

<p class="back_to_top">[ <a href="#top">Back to top</a> ]</p>

<h2 id="troubleshoot-bioconductor-packages">Troubleshoot Package Installations</h2>

Use the commands

    library(BiocInstaller)
	biocValid()             ## R version 3.0 or later

to flag packages that are either out-of-date or too new for your
version of _Bioconductor_. The output suggests ways to solve identified
problems, and the help page `?biocValid` lists arguments influencing
the behavior of the function.

<h3 id="troubleshoot-biocinstaller">Troubleshoot BiocInstaller</h3>

If you see a message like this:

    BiocInstaller version 3.2 is too old for R version 3.3

...do the following:

* Quit your R session
* Start a new session with `R --vanilla`
* Run the command `remove.packages("BiocInstaller", lib=.libPaths())`
* Repeat that command until R says there is no such package.
* Run the command `source("https://bioconductor.org/biocLite.R")`
* Run `biocValid()` to ensure your installed packages are
  valid for the current version of _Bioconductor_, and follow
  the instructions it gives you.




<p class="back_to_top">[ <a href="#top">Back to top</a> ]</p>

<h2 id="why-biocLite">Why Use biocLite()?</h2>

`biocLite()` is the recommended way to install _Bioconductor_
packages. There are several reasons for preferring this to the
'standard' way in which R pacakges are installed via
`install.packages()`.

_Bioconductor_ has a repository and release schedule that differs from R
(_Bioconductor_ has a 'devel' branch to which new packages and updates
are introduced, and a stable 'release' branch emitted once every 6
months to which bug fixes but not new features are introduced).

A consequence of the mismatch between R and _Bioconductor_ release
schedules is that the _Bioconductor_ version identified by
`install.packages()` is sometimes not the most recent 'release'
available. For instance, an R minor version may be introduced some
months before the next Bioc release. After the Bioc release the users
of the R minor version will be pointed to an out-of-date version of
_Bioconductor_.

A consequence of the distinct 'devel' branch is that
`install.packages()` sometimes points only to the 'release'
repository, whereas _Bioconductor_ developers and users wanting
leading-edge features wish to access the _Bioconductor_ 'devel'
repository. For instance, the _Bioconductor_ 3.0 release is available
for R.3.1.x, so _Bioconductor_ developers and leading-edge users need to
be able to install the devel version of _Bioconductor_ packages into the
same version (though perhaps different instance or at least library
location) of R that supports version 2.14 of _Bioconductor_.

An indirect consequence of _Bioconductor_'s structured release is that
packages generally have more extensive dependencies with one another,
both explicitly via the usual package mechanisms and implicitly
because the repository, release structure, and _Bioconductor_ community
interactions favor re-use of data representations and analysis
concepts across packages. There is thus a higher premium on knowing
that packages are from the same release, and that all packages are
current within the release.

These days, the main purpose of
`source("https://bioconductor.org/biocLite.R")` is to install and
attach the 'BiocInstaller' package.

In a new installation, the script installs the most recent version of
the BiocInstaller package relevant to the version of R in use,
regardless of the relative times of R and _Bioconductor_ release
cycles. The BiocInstaller package serves as the primary way to
identify the version of _Bioconductor_ in use

    > library(BiocInstaller)
    Bioconductor version 2.14 (BiocInstaller 1.14.2), ?biocLite for help

Since new features are often appealing to users, but at the same time
require an updated version of _Bioconductor_, the source() command
evaluated in an out-of-date R will nudge users to upgrade, e.g., in
R-2.15.3

    > source("https://bioconductor.org/biocLite.R")
    A new version of Bioconductor is available after installing the most
      recent version of R; see http://bioconductor.org/install

The `biocLite()` function is provided by BiocInstaller. This is a
wrapper around `install.packages`, but with the repository chosen
according to the version of _Bioconductor_ in use, rather than to the
version relevant at the time of the release of R.

`biocLite()` also nudges users to remain current within a release, by
default checking for out-of-date packages and asking if the user would
like to update

    > biocLite()
    BioC_mirror: http://bioconductor.org
    Using Bioconductor version 2.14 (BiocInstaller 1.14.2), R version
      3.1.0.
    Old packages: 'BBmisc', 'genefilter', 'GenomicAlignments',
      'GenomicRanges', 'IRanges', 'MASS', 'reshape2', 'Rgraphviz',
      'RJSONIO', 'rtracklayer'
    Update all/some/none? [a/s/n]:

The BiocInstaller package provides facilities for switching to the
'devel' version of _Bioconductor_

    > BiocInstaller::useDevel()
    Installing package into ‘/home/mtmorgan/R/x86_64-unknown-linux-gnu-library/3.1’
    (as ‘lib’ is unspecified)
    trying URL 'http://bioconductor.org/packages/3.0/bioc/src/contrib/BiocInstaller_1.15.5.tar.gz'
    Content type 'application/x-gzip' length 14144 bytes (13 Kb)
    opened URL
    ==================================================
    downloaded 13 Kb

    * installing *source* package ‘BiocInstaller’ ...
    ...
    Bioconductor version 3.0 (BiocInstaller 1.15.5), ?biocLite for help
    'BiocInstaller' changed to version 1.15.5

(at some points in the R / _Bioconductor_ release cycle use of 'devel'
requires use of a different version of R itself, in which case the
attempt to `useDevel()` fails with an appropriate message).

The BiocInstaller package also provides `biocValid()` to test that the
installed packages are not a hodgepodge from different _Bioconductor_
releases (the 'too new' packages have been installed from source
rather than a repository; regular users would seldom have these).

    > biocValid()

    * sessionInfo()

    R version 3.1.0 Patched (2014-05-06 r65533)
    Platform: x86_64-unknown-linux-gnu (64-bit)
    ...

    * Out-of-date packages
    ...
    update with biocLite()

    * Packages too new for Bioconductor version '3.0'
    ...
    downgrade with biocLite(c("ShortRead", "BatchJobs"))

    Error: 9 package(s) out of date; 2 package(s) too new

For users who spend a lot of time in _Bioconductor_, the features
outlined above become increasingly important and `biocLite()` is much
preferred to `install.packages()`.

<p class="back_to_top">[ <a href="#top">Back to top</a> ]</p>

<h2 id="preconfigured">Pre-configured <em>Bioconductor</em></h2>

_Bioconductor_ is also available as a set of
[Amazon Machine Images (AMIs)](/help/bioconductor-cloud-ami/) and
[Docker images](/help/docker/).

<p class="back_to_top">[ <a href="#top">Back to top</a> ]</p>
