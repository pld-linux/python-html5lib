%define		module	html5lib
Summary:	HTML parser/tokenizer based on the WHATWG HTML5 specification
Summary(pl.UTF-8):	Analizator i tokenizer HTML-a oparty na specyfikacji WHATWG HTML5
Name:		python-%{module}
Version:	0.10
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://html5lib.googlecode.com/files/%{module}-%{version}.zip
# Source0-md5:	cc69960c4153d89bf5b998a06b8cdced
URL:		http://code.google.com/p/html5lib/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML parser/tokenizer based on the WHATWG HTML5 specification.

%description -l pl.UTF-8
Analizator i tokenizer HTML-a oparty na specyfikacji WHATWG HTML5.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py_sitescriptdir}/%{module}
