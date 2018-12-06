# https://github.com/jackpal/gateway
%global goipath github.com/jackpal/gateway
%global commit  cbcf4e3f3baee7952fc386c8b2534af4d267c875
%global date    20180407

%gometa

Name:           %{goname}
Version:        1.0.4
Release:        0.8%{?dist}
Summary:        Discovering the address of a LAN gateway in go
License:        BSD

URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup -p1


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Oct 24 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.4-0.8.20180407gitcbcf4e3
- Use forgeautosetup instead of gosetup.

* Sun Sep 02 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.4-0.7.20180407gitcbcf4e3
- Update to use spec 3.0.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-0.6.gitcbcf4e3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Apr 11 2018 Fabio Valentini <decathorpe@gmail.com> - 1.0.4-0.5.gitcbcf4e3
- Bump to commit cbcf4e3.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-0.4.git5795ac8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-0.3.git5795ac8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-0.2.git5795ac8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 01 2017 Fabio Valentini <decathorpe@gmail.com> - 1.0.4-0.1.git5795ac8
- First package for Fedora

