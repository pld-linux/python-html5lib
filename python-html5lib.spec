#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	tests	# py.test tests
#
%define		module	html5lib
Summary:	HTML parser/tokenizer based on the WHATWG HTML5 specification
Summary(pl.UTF-8):	Analizator i tokenizer HTML-a oparty na specyfikacji WHATWG HTML5
Name:		python-%{module}
Version:	0.999999999
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://github.com/html5lib/html5lib-python/releases
Source0:	https://github.com/html5lib/html5lib-python/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	a81446ef3ce3ef18f5e8e242b7072b83
URL:		https://github.com/html5lib/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools >= 18.5
%if %{with tests}
BuildRequires:	python-flake8
BuildRequires:	python-mock
%if "%{py_ver}" < "2.7"
BuildRequires:	python-ordereddict
%endif
BuildRequires:	python-pytest
BuildRequires:	python-pytest-expect >= 1.1
BuildRequires:	python-pytest-expect < 2.0
BuildRequires:	python-six
BuildRequires:	python-webencodings
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools >= 18.5
%if %{with tests}
BuildRequires:	python3-flake8
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-expect >= 1.1
BuildRequires:	python3-pytest-expect < 2.0
BuildRequires:	python3-six
BuildRequires:	python3-webencodings
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML parser/tokenizer based on the WHATWG HTML5 specification.

%description -l pl.UTF-8
Analizator i tokenizer HTML-a oparty na specyfikacji WHATWG HTML5.

%package -n python3-%{module}
Summary:	HTML parser/tokenizer based on the WHATWG HTML5 specification
Summary(pl.UTF-8):	Analizator i tokenizer HTML-a oparty na specyfikacji WHATWG HTML5
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
HTML parser/tokenizer based on the WHATWG HTML5 specification.

%description -n python3-%{module} -l pl.UTF-8
Analizator i tokenizer HTML-a oparty na specyfikacji WHATWG HTML5.

%prep
%setup -q -n %{module}-python-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
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
%doc AUTHORS.rst CHANGES.rst LICENSE README.rst
%{py_sitescriptdir}/html5lib-%{version}-py*.egg-info
%{py_sitescriptdir}/html5lib
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGES.rst LICENSE README.rst
%{py3_sitescriptdir}/html5lib-%{version}-py*.egg-info
%{py3_sitescriptdir}/html5lib
%endif
