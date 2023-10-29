# vim: sw=4:ts=4:et


%define relabel_files() \
restorecon -R /usr/local/bin/logdaemon.py; \

%define selinux_policyver 38.30-1

Name:   logdaemon_selinux
Version:	1.0
Release:	1%{?dist}
Summary:	SELinux policy module for logdaemon

Group:	System Environment/Base		
License:	GPLv2+	
# This is an example. You will need to change it.
URL:		http://HOSTNAME
Source0:	logdaemon.pp
Source1:	logdaemon.if
Source2:	logdaemon_selinux.8


Requires: policycoreutils, libselinux-utils
Requires(post): selinux-policy-base >= %{selinux_policyver}, policycoreutils
Requires(postun): policycoreutils
BuildArch: noarch

%description
This package installs and sets up the  SELinux policy security module for logdaemon.

%install
install -d %{buildroot}%{_datadir}/selinux/packages
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/selinux/packages
install -d %{buildroot}%{_datadir}/selinux/devel/include/contrib
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/selinux/devel/include/contrib/
install -d %{buildroot}%{_mandir}/man8/
install -m 644 %{SOURCE2} %{buildroot}%{_mandir}/man8/logdaemon_selinux.8
install -d %{buildroot}/etc/selinux/targeted/contexts/users/


%post
semodule -n -i %{_datadir}/selinux/packages/logdaemon.pp
if /usr/sbin/selinuxenabled ; then
    /usr/sbin/load_policy
    %relabel_files

fi;
exit 0

%postun
if [ $1 -eq 0 ]; then
    semodule -n -r logdaemon
    if /usr/sbin/selinuxenabled ; then
       /usr/sbin/load_policy
       %relabel_files

    fi;
fi;
exit 0

%files
%attr(0600,root,root) %{_datadir}/selinux/packages/logdaemon.pp
%{_datadir}/selinux/devel/include/contrib/logdaemon.if
%{_mandir}/man8/logdaemon_selinux.8.*


%changelog
* Sun Oct 29 2023 YOUR NAME <YOUR@EMAILADDRESS> 1.0-1
- Initial version

