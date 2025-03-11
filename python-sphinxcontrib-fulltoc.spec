#
# Conditional build:
%bcond_without	doc	# Sphinx documentation (disable for bootstrap)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Include a full table of contents in your Sphinx HTML sidebar
Summary(pl.UTF-8):	Dołączanie pełnego spisu treści w pasku nawigacji HTML ze Sphinksa
Name:		python-sphinxcontrib-fulltoc
Version:	1.2.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-fulltoc/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-fulltoc/sphinxcontrib-fulltoc-%{version}.tar.gz
# Source0-md5:	1b4326b588ae9e7bfe69b51670b74cfb
URL:		https://pypi.org/project/sphinxcontrib-fulltoc/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-pbr
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
# already installed package
BuildRequires:	python-sphinxcontrib-fulltoc
BuildRequires:	sphinx-pdg-2
%endif
Requires:	python-modules >= 1:2.7
Requires:	python-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinxcontrib-fulltoc is an extension for the Sphinx documentation
system that changes the HTML output to include a more detailed table
of contents in the sidebar. By default Sphinx only shows the local
headers for the current page. With the extension installed, all of the
page titles are included, and the local headers for the current page
are also included in the appropriate place within the document.

%description -l pl.UTF-8
sphinxcontrib-fulltoc to rozszerzenie systemu dokumentacji Sphinx,
zmieniające wyjście HTML tak, aby zawierało bardziej szczegółowy spis
treści na pasku bocznym. Domyślnie Sphinx pokazuje tylko lokalne
nagłówki dla bieżącej strony. Po zainstalowaniu rozszerzenia dołączane
są tytuły wszystkich stron, a lokalne nagłówki bieżącej strony są
dołączane także we właściwym miejscu dokumentu.

%package -n python3-sphinxcontrib-fulltoc
Summary:	Include a full table of contents in your Sphinx HTML sidebar
Summary(pl.UTF-8):	Dołączanie pełnego spisu treści w pasku nawigacji HTML ze Sphinksa
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3
Requires:	python3-sphinxcontrib

%description -n python3-sphinxcontrib-fulltoc
sphinxcontrib-fulltoc is an extension for the Sphinx_ documentation
system that changes the HTML output to include a more detailed table
of contents in the sidebar. By default Sphinx only shows the local
headers for the current page. With the extension installed, all of the
page titles are included, and the local headers for the current page
are also included in the appropriate place within the document.

%description -n python3-sphinxcontrib-fulltoc -l pl.UTF-8
sphinxcontrib-fulltoc to rozszerzenie systemu dokumentacji Sphinx,
zmieniające wyjście HTML tak, aby zawierało bardziej szczegółowy spis
treści na pasku bocznym. Domyślnie Sphinx pokazuje tylko lokalne
nagłówki dla bieżącej strony. Po zainstalowaniu rozszerzenia dołączane
są tytuły wszystkich stron, a lokalne nagłówki bieżącej strony są
dołączane także we właściwym miejscu dokumentu.

%package apidocs
Summary:	API documentation for Python sphinxcontrib-fulltoc module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona sphinxcontrib-fulltoc
Group:		Documentation

%description apidocs
API documentation for Python sphinxcontrib-fulltoc module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona sphinxcontrib-fulltoc.

%prep
%setup -q -n sphinxcontrib-fulltoc-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
# incompatible with python3 (as of 1.2.0)
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst announce.rst
%{py_sitescriptdir}/sphinxcontrib/fulltoc.py[co]
%{py_sitescriptdir}/sphinxcontrib_fulltoc-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_fulltoc-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-fulltoc
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst announce.rst
%{py3_sitescriptdir}/sphinxcontrib/fulltoc.py
%{py3_sitescriptdir}/sphinxcontrib/__pycache__/fulltoc.cpython-*.py[co]
%{py3_sitescriptdir}/sphinxcontrib_fulltoc-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_fulltoc-%{version}-py*-nspkg.pth
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/build/html/{_static,*.html,*.js}
%endif
