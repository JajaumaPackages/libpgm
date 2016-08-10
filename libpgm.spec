Name:           libpgm
Version:        5.2.122
Release:        2%{?dist}
Summary:        An open source implementation of the Pragmatic General Multicast

License:        %{lic_3rdparty}
URL:            http://miru.hk/openpgm/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/openpgm/libpgm-%{version}~dfsg.tar.gz

BuildRequires:  python


%description
OpenPGM is an open source implementation of the Pragmatic General Multicast
(PGM) specification in RFC 3208 available at www.ietf.org. PGM is a reliable
and scalable multicast protocol that enables receivers to detect loss, request
retransmission of lost data, or notify an application of unrecoverable loss.
PGM is a receiver-reliable protocol, which means the receiver is responsible
for ensuring all data is received, absolving the sender of reception
responsibility. PGM runs over a best effort datagram service, currently OpenPGM
uses IP multicast but could be implemented above switched fabrics such as
InfiniBand.

PGM is appropriate for applications that require duplicate-free multicast data
delivery from multiple sources to multiple receivers. PGM does not support
acknowledged delivery, nor does it guarantee ordering of packets from multiple
senders.

PGM is primarly used on internal networks to help integrate disparate systems
through a common communication platform. A lack of IPv4 multicast-enabled
infrastructure leads to limited capability for internet applications, IPv6
promotes multicast to be a part of the core functionality of IP but may still
be disabled on core routers. Support of Source-Specific Multicast (SSM) allows
for improved WAN deployment by allowing end-point router filtering of unwanted
source traffic.


%package        devel
Summary:        Development files and libraries for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig


%description    devel
Headers and libraries for developing applications that use %{name}
functionality.


%prep
%setup -q -n libpgm-%{version}~dfsg/openpgm/pgm


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig


%files
%doc COPYING LICENSE README
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/openpgm-5.2.pc


%changelog
* Wed Aug 10 2016 Jajauma's Packages <jajauma@yandex.ru> - 5.2.122-2
- Public release
