Name:		python-pdm
Version:	2.22.3
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/p/pdm/pdm-%{version}.tar.gz
Summary:	A modern Python package and dependency manager supporting the latest PEP standards
URL:		https://pypi.org/project/pdm/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(pdm-backend)
BuildSystem:	python
BuildArch:	noarch

%description
A modern Python package and dependency manager supporting the latest PEP standards

%prep
%autosetup -p1 -n pdm-%{version}

%files
%{_bindir}/pdm
%{py_sitedir}/pdm
%{py_sitedir}/pdm-*.*-info
