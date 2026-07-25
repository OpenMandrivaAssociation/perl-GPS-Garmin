%define upstream_name		perl-GPS
%define upstream_version	0.17

Name:		%{upstream_name}-Garmin
Version:	%{upstream_version}
Release:	5
License:	GPL+ or Artistic
Summary:	Perl interface to GPS equipment using the Garmin Protocol
Group:		Development/Perl
Url:		https://metacpan.org/dist/perl-GPS
Source0:	https://cpan.metacpan.org/authors/id/S/SR/SREZIC/perl-GPS-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Device::SerialPort)
BuildArch:	noarch

%description
GPS::Garmin allow the connection and use of of a GPS receiver in perl
scripts. Currently only the GRMN/GRMN protocol is implemented but NMEA
is a work in progress.

This module currently works with Garmin GPS II+ equipments, but should
work on most Garmin receivers that support the GRMN/GRMN protocol.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/GPS
%{_mandir}/man3/GPS*


%changelog
* Thu Nov 04 2010 Jani Välimaa <wally@mandriva.org> 0.170.0-1mdv2011.0
+ Revision: 593411
- use perl_convert_version macro
- fix group, license, url, source, summary and description
- tag package as noarch
- add BR
- provide perl-GPS
- install files to a correct location

  + Thomas Spuhler <tspuhler@mandriva.org>
    - corrected Group to Development/Perl

* Sun Oct 31 2010 Thomas Spuhler <tspuhler@mandriva.org> 0.17-1mdv2011.0
+ Revision: 591252
- import perl-GPS-Garmin

