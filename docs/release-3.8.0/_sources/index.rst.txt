.. image:: assets/Bento-Header-Logo.png
    :alt: Bento Logo

|

===========================
Bento Project Documentation
===========================

Welcome! This is the documentation site for the Bento Project. It describes the Bento project's background and explains how to set up a data sharing platform using the Bento framework.

Bento is a software framework being built to support NCI’s `Cancer Research Data Commons <https://datascience.cancer.gov/data-commons>`_ projects, including `Integrated Canine Data Commons <https://datacommons.cancer.gov/repository/integrated-canine-data-commons>`_ (`ICDC <https://caninecommons.cancer.gov/#/>`_), and `Clinical Trial Data Commons <https://datacommons.cancer.gov/repository/clinical-trial-data-commons>`_ (CTDC).

This site provides you with the background and instructions you need to set up your own data sharing platform using Bento.

.. image:: assets/bento_tools_demo_site_thumb.png
   :target: https://bento-tools\.org/#/

Checkout our example site using Bento framework! `Bento-tools <https://bento-tools.org/#/>`_

Bento Documentation (this site): `https://cbiit.github.io/bento-docs/ <https://cbiit.github.io/bento-docs/>`_

GitHub: `https://github.com/CBIIT/bento-docs/ <https://github.com/CBIIT/bento-docs/>`_

.. toctree::
    :caption: Welcome
    :maxdepth: 1

    overview

.. toctree::
    :maxdepth: 1
    :numbered:
    :caption: Installation

    installation/bento-quick-start
    installation/installing-bento-on-your-local-machine
    installation/bento_aws_installation
    installation/bento_gcp_cloud_run_installation
    installation/bento_gcp_gke_installation

.. toctree::
    :maxdepth: 1
    :numbered:
    :caption: Configuration

    configuration/global-ui-elements
    configuration/landing-page
    configuration/program-listing-page
    configuration/program-detail-page
    configuration/arm-detail-page
    configuration/case-detail-page
    configuration/dashboard
    configuration/dashboard-facet-search-sidebar
    configuration/dashboard-tabs-and-tables
    configuration/cart-workflow
    configuration/static-pages
    configuration/authentication

.. toctree::
    :maxdepth: 1
    :numbered:
    :caption: Data and Modeling

    data-and-modeling/data-loader
    data-and-modeling/model-converter
    data-and-modeling/file-copier
    data-and-modeling/bento-backend
    data-and-modeling/Bento_TailoRx_Data_Dictionary
    data-and-modeling/bento-tailorx-data-dicionary-relationships
    data-and-modeling/bento-data-model-attributes

.. toctree::
    :maxdepth: 1
    :numbered:
    :caption: Project Info

    project-info/Bento-Glossary
    project-info/gitflow
    project-info/meet-the-team
    project-info/license
    project-info/change-log
