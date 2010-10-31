Name:		perl-GPS-Garmin
Version: 	0.17
Release:	%mkrel 1
Summary: 	GPS-Garmin - Perl interface to GPS equipment using the Garmin Protocol
Group:		Communications
License:	Artistic
URL: 		http://www.cpan.org/authors/id/J/JO/JOAOP/
Source0: 	http://www.cpan.org/authors/id/J/JO/JOAOP/perl-GPS-%{version}.tar.gz
BuildRequires:  perl-devel



%description
use GPS::Garmin;
$gps = new GPS::Garmin(  'Port'      => '/dev/ttyS0', 
'Baud'      => 9600,
);
To transfer current position, and direction symbols:
($latsign,$lat,$lonsign,$lon) = $gps->get_position;
To transfer current time:
($sec,$min,$hour,$mday,$mon,$year) = $gps->get_time;
To transfer trackpoints:
$gps->prepare_transfer("trk");  
while($gps->records) {
($lat,$lon,$time) = $gps->grab;
}
To transfer Waypoints:
$gps->prepare_transfer("wpt");  
while($gps->records) {
($title,$lat,$lon,$desc) = $gps->grab;
}

%prep
%setup -q -n perl-GPS-%{version} 


%build

%__perl Makefile.PL \

%__make


%install
%__rm -rf %{buildroot}
%makeinstall_std


# make some directories
install -d %{buildroot}%{_mandir}/man3
#mv %{buildroot}  /usr/local/share/man/man3/* %{buildroot}%{_mandir}/man3/

%clean
%__rm -rf %{buildroot}

%files
%defattr(-, root, root)
%dir %{perl_sitelib}/GPS
%{perl_sitelib}/GPS/*
/usr/local/share/man/man3/*

