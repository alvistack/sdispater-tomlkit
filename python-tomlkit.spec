# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-tomlkit
Epoch: 100
Version: 0.11.5
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
fdupes -qnrps %{buildroot}%{python3_sitelib}

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
%{python3_sitelib}/*
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
%{python3_sitelib}/*
%endif

%changelog
