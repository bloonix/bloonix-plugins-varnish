Summary: Bloonix plugins for Varnish.
Name: bloonix-plugins-varnish
Version: 0.5
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core
AutoReqProv: no

%description
bloonix-plugins-varnish provides plugins to check the varnish daemon.

%define blxdir /usr/lib/bloonix
%define docdir %{_docdir}/%{name}-%{version}

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Configure.PL --prefix /usr
%{__make}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{docdir}
install -c -m 0444 LICENSE ${RPM_BUILD_ROOT}%{docdir}/
install -c -m 0444 ChangeLog ${RPM_BUILD_ROOT}%{docdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Tue Mar 29 2016 Jonny Schulz <js@bloonix.de> - 0.5-1
- Extra release because the gpg key of bloonix is updated.
* Tue Nov 18 2014 Jonny Schulz <js@bloonix.de> - 0.4-1
- Fixed counter statistics.
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.3-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.2-1
- Licence added and old releases deleted.
* Mon Jul 11 2014 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.
