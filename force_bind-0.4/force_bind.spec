Summary:	Force binding to a specif address and/or port
Name:		force_bind
Version:	0.4
Release:	1
License:	LGPL
Group:		Applications/Network
Source:		http://kernel.embedromix.ro/us/Conn/%{name}-%{version}.tar.gz
URL:		http://kernel.embedromix.ro/us/
Packager:	Catalin(ux) M BOIE <catab@embedromix.ro>
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot


%description
It uses LD_PRELOAD to hijack 'bind' system call. Environment variables
FORCE_BIND_ADDRESS and FORCE_BIND_PORT can be used to control it.

%prep
%setup

%build
%configure
make

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}
make install DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%attr (-,root,root)
%dir /usr/lib/*
%doc README LICENSE Changelog
