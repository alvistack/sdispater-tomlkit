%global debug_package %{nil}

Name: python-tomlkit
Epoch: 100
Version: 0.8.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Style preserving TOML library
License: MIT
URL: https://github.com/sdispater/tomlkit/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
TOML Kit is a 1.0.0rc1-compliant TOML library. It includes a parser that
preserves all comments, indentations, whitespace and internal element
ordering, and makes them accessible and editable via an intuitive API.
You can also create new TOML documents from scratch using the provided
helpers. Part of the implementation as been adapted, improved and fixed
from Molten.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-tomlkit
Summary: Style preserving TOML library
Requires: python3
Provides: python3-tomlkit = %{epoch}:%{version}-%{release}
Provides: python3dist(tomlkit) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tomlkit = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tomlkit) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tomlkit = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tomlkit) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-tomlkit
TOML Kit is a 1.0.0rc1-compliant TOML library. It includes a parser that
preserves all comments, indentations, whitespace and internal element
ordering, and makes them accessible and editable via an intuitive API.
You can also create new TOML documents from scratch using the provided
helpers. Part of the implementation as been adapted, improved and fixed
from Molten.

%files -n python%{python3_version_nodots}-tomlkit
%license LICENSE
%{python3_sitelib}/tomlkit*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-tomlkit
Summary: Style preserving TOML library
Requires: python3
Provides: python3-tomlkit = %{epoch}:%{version}-%{release}
Provides: python3dist(tomlkit) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-tomlkit = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(tomlkit) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-tomlkit = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(tomlkit) = %{epoch}:%{version}-%{release}

%description -n python3-tomlkit
TOML Kit is a 1.0.0rc1-compliant TOML library. It includes a parser that
preserves all comments, indentations, whitespace and internal element
ordering, and makes them accessible and editable via an intuitive API.
You can also create new TOML documents from scratch using the provided
helpers. Part of the implementation as been adapted, improved and fixed
from Molten.

%files -n python3-tomlkit
%license LICENSE
%{python3_sitelib}/tomlkit*
%endif

%changelog
