Summary:	Collection of clustering tools
Name:		clusterit
Version:	2.5
Release:	%mkrel 3
License:	BSD
Group:		Networking/Remote access
URL:		http://clusterit.sourceforge.net/
Source:		%{name}-%{version}.tar.gz
Source1:	dshbak.sh
BuildRequires:  libx11-devel
BuildRequires:	ncurses-devel
Requires:	openssh-clients, rsh, gawk
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is a collection of clustering tools, to turn your ordinary 
everyday pile of UNIX workstations into a speedy parallel beast.
dsh : run a command on a cluster of machines.  dshbak : format the 
output of dsh. barrier, barrierd : synchronize a process on a number 
of machines. jsd : simple command scheduling daemon for remote execution. 
jsh : run scheduled commands on remote machines. run : run a command 
on a machine at random. seq : run a command on a cluster in sequence. 
pcp : copy a file to a cluster of machines. pdf : display free disk space
across a group of machines. prm : delete a file or files on a cluster 
of machines. rvt : a specialized VT100 emulator for the X window system. 
dvt : clustersed quickly dissect cluster files.

%prep
%setup -q

%build
mkdir -p %{buildroot}/%{name}-%{version}/tools/
install -m644 %{SOURCE1} %{buildroot}/%{name}-%{version}/tools/dshbak.sh
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root) 
%doc INSTALL CHANGES README html/*.html html/man/*.html
%{_mandir}/man1/*
%{_bindir}/*

