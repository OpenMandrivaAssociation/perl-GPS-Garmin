%define upstream_name		perl-GPS
%define upstream_version	0.17

Name:		%{upstream_name}-Garmin
Version: 	%perl_convert_version %{upstream_version}
Release:	%mkrel 1
License:	GPL+ or Artistic
Summary: 	Perl interface to GPS equipment using the Garmin Protocol
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/GPS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Device::SerialPort)
BuildArch:	noarch
Provides:	%{upstream_name} = %{version}-%{release}

%description
GPS::Garmin allow the connection and use of of a GPS receiver in perl
scripts. Currently only the GRMN/GRMN protocol is implemented but NMEA
is a work in progress.

This module currently works with Garmin GPS II+ equipments, but should
work on most Garmin receivers that support the GRMN/GRMN protocol.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make


%install
%__rm -rf %{buildroot}
%makeinstall_std

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc Changes README
%{perl_vendorlib}/GPS
%{_mandir}/man3/GPS*
