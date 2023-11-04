%global pypi_name torchdata
%global pypi_version 0.7

%bcond_with gitcommit
%if %{with gitcommit}
# The top of the 0.7 branch - update to whatever..
%global commit0 4e255c95c76b1ccde4f6650391c0bc30650d6dbe
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%endif

Name:           python-%{pypi_name}
Version:        %{pypi_version}.0
Release:        1%{?dist}
Summary:        A PyTorch repo for data loading and utilities.

License:        BSD-3-Clause
URL:            https://github.com/pytorch/data
%if %{with gitcommit}
Source0:        %{url}/archive/%{commit0}/data-%{shortcommit0}.tar.gz
%else
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/data-%{version}.tar.gz
# Do not use git submodules
Patch0:         0001-Prepare-torchdata-setup-for-fedora.patch
%endif

# Limit to these because that is what torch is on
ExclusiveArch:  x86_64 aarch64
%global toolchain clang

# Empty %files file .../rpmbuild/BUILD/data-0.7.0/debugsourcefiles.list
%global debug_package %{nil}

BuildRequires:  python3-devel
BuildRequires:  python3dist(packaging)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(requests)
BuildRequires:  python3dist(torch)
BuildRequires:  python3dist(urllib3)

%description
torchdata is a library of common modular data loading primitives for
easily constructing flexible and performant data pipelines.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
torchdata is a library of common modular data loading primitives for
easily constructing flexible and performant data pipelines.

%prep
%if %{with gitcommit}
%autosetup -p1 -n data-%{commit0}
%else
%autosetup -p1 -n data-%{version}
%endif

rm -rf third_party/*

# pyproject_ is broken it is generate_buildrequires looks for
# python3-cmake and python3-ninja, revert to old py3_

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%dir %{python3_sitelib}/%{pypi_name}
%dir %{python3_sitelib}/%{pypi_name}/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/dataloader2
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/communication
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/communication/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/graph
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/graph/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/random
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/random/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/utils
%dir %{python3_sitelib}/%{pypi_name}/dataloader2/utils/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes
%dir %{python3_sitelib}/%{pypi_name}/datapipes/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/load
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/load/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/transform
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/transform/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/util
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/util/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/util/protobuf_template
%dir %{python3_sitelib}/%{pypi_name}/datapipes/iter/util/protobuf_template/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map/load
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map/load/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map/transform
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map/transform/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map/util
%dir %{python3_sitelib}/%{pypi_name}/datapipes/map/util/__pycache__
%dir %{python3_sitelib}/%{pypi_name}/datapipes/utils
%dir %{python3_sitelib}/%{pypi_name}/datapipes/utils/__pycache__

%{python3_sitelib}/%{pypi_name}/{*.py,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/dataloader2/{*.py,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/dataloader2/{communication,graph,random,utils}/{*.py,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/datapipes/{*.py,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/datapipes/iter/{*.py,*.pyi,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/datapipes/iter/{load,transform,util}/{*.py,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/datapipes/iter/util/protobuf_template/{*.py,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/datapipes/map/{*.py,*.pyi,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/datapipes/map/{load,transform,util}/{*.py,__pycache__/*.pyc}
%{python3_sitelib}/%{pypi_name}/datapipes/utils/{*.py,__pycache__/*.pyc}

%{python3_sitelib}/%{pypi_name}-%{version}-py3.12.egg-info

%changelog
* Sat Oct 14 2023 Tom Rix <trix@redhat.com> - 0.7.0-1
- Initial package.

