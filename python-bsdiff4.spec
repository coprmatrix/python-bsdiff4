#
# spec file for package python-bsdiff4
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           python-bsdiff4
Version:        1.2.5
Release:        0
Summary:        binary diff and patch using the BSDIFF4-format
License:        BSD (FIXME:No SPDX)
URL:            https://github.com/ilanschnell/bsdiff4
Source:         bsdiff4-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
%python_subpackages

%description
binary diff and patch using the BSDIFF4-format

%prep
%autosetup -p1 -n bsdiff4-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bspatch4
%python_clone -a %{buildroot}%{_bindir}/bsdiff4
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check


%post
%python_install_alternative bspatch4 bsdiff4

%postun
%python_uninstall_alternative bspatch4

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/bspatch4
%python_alternative %{_bindir}/bsdiff4
%{python_sitearch}/bsdiff4
%{python_sitearch}/bsdiff4-%{version}.dist-info

%changelog
