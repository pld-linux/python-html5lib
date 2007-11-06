%define		module	html5lib
Summary:	HTML parser/tokenizer based on the WHATWG HTML5 specification
Name:		python-%{module}
Version:	0.10
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://html5lib.googlecode.com/files/%{module}-%{version}.zip
# Source0-md5:	cc69960c4153d89bf5b998a06b8cdced
URL:		http://code.google.com/p/html5lib/
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML parser/tokenizer based on the WHATWG HTML5 specification

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

install -d $RPM_BUILD_ROOT{%{_bindir},%{_examplesdir}/%{name}-%{version}}

%py_postclean $RPM_BUILD_ROOT%{py_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%{py_sitescriptdir}/%{module}
