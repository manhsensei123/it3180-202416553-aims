# Câu hỏi thảo luận Lab 04

1. **Vì sao phải chuẩn bị thông tin phát hành (`__version__`, `CHANGELOG.md`) trên `master` trước mà không sửa trực tiếp trên nhánh `release`?**
   - Vì trong Release Flow, nhánh `release/*` không bao giờ merge ngược lại vào `master`. Nếu sửa số phiên bản và `CHANGELOG.md` trực tiếp trên `release/lab04`, nhánh `master` sẽ bị thiếu lịch sử `CHANGELOG` và mốc phiên bản `1.0.0`, buộc phải cherry-pick thủ công ngược lại. Chuẩn bị trên `master` trước giúp dòng lịch sử chính luôn đầy đủ và nhất quán ngay tại thời điểm phân nhánh.

2. **Vì sao `release/*` không merge ngược vào `master`? So sánh với GitFlow.**
   - Trong Release Flow của học phần, mỗi nhánh `release/*` đóng vai trò là dòng bảo trì độc lập cho một phiên bản đã phát hành (ví dụ `1.0.x`), trong khi `master` đã tiến lên phiên bản mới hơn (`1.1.0`). Nếu merge ngược `release/*` vào `master` sẽ gây xung đột hoặc ghi đè lùi số phiên bản và cấu hình cũ lên mã nguồn mới; thay vào đó, các bản vá lỗi cần thiết sẽ được lan truyền có chọn lọc bằng `cherry-pick`.
   - So với **GitFlow**: GitFlow duy trì song song hai nhánh dài hạn `main` và `develop`, nhánh `release/*` là nhánh ngắn hạn tách từ `develop` để hoàn thiện rồi merge vào cả `main` lẫn `develop` trước khi xóa đi. Ngược lại, **Release Flow** chỉ dùng một nhánh phát triển chính (`master`) và giữ các nhánh `release/*` tồn tại lâu dài để bảo trì song song nhiều phiên bản.

3. **Vì sao đánh số phiên bản lên `1.0.0` mà không phải `0.4.0`?**
   - Theo quy ước Semantic Versioning (SemVer), dải phiên bản `0.y.z` (`v0.1.0` – `v0.3.0` ở Lab 01–03) dành cho giai đoạn phát triển khởi đầu khi chức năng và giao diện chưa ổn định. Ở Lab 04, ứng dụng AIMS-mini đã hoàn thiện đầy đủ tập chức năng cốt lõi, vượt qua kiểm thử đơn vị và chính thức phát hành baseline ổn định đầu tiên cho người dùng (qua GitHub Release), nên cần chuyển sang `MAJOR = 1` tức `1.0.0`.
