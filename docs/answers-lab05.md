# Câu hỏi thảo luận Lab 05

1. **Ưu, nhược điểm của chính sách `upstream first` (sửa trên `master` trước) so với `release first` (sửa trên `release/*` trước)?**
   - **Upstream first (như mô hình của Microsoft):**
     - *Ưu điểm:* Đảm bảo lỗi được giải quyết triệt để ngay tại gốc `master`, không bao giờ xảy ra tình trạng quên đưa bản vá lên bản phát hành tương lai (tránh regression bug).
     - *Nhược điểm:* Khi cherry-pick lùi từ `master` về các bản phát hành cũ (`release/*`), mã nguồn trên `master` có thể đã thay đổi quá nhiều khiến việc cherry-pick dễ bị xung đột phức tạp.
   - **Release first (mô hình học phần áp dụng):**
     - *Ưu điểm:* Bản vá được xây dựng và kiểm thử trực tiếp trên chính môi trường của bản phát hành đang chạy lỗi (`release/lab04`), cô lập rủi ro, phát hành bản vá `v1.0.1` tới người dùng nhanh nhất có thể.
     - *Nhược điểm:* Đòi hỏi quy trình kỷ luật nghiêm ngặt để lan truyền bản vá ngược lại cho `master` và các nhánh release khác; nếu quên thì phiên bản tương lai sẽ bị tái phát lỗi cũ.

2. **Nếu quên lan truyền bản sửa sang `release/lab05`, lệnh nào ở Phần F sẽ phát hiện?**
   - Lệnh `git log --all --oneline --grep "cherry picked from commit <FIX_SHA>"` sẽ chỉ tìm thấy 1 commit cherry-pick (trên `master`) thay vì đủ 2 commit (trên `master` và `release/lab05`).
   - Hoặc vòng lặp chạy thử nghiệm thực tế hàm `search_by_title([D('The Lion King')], 'lion')` trên `v1.1.0` sẽ in ra `0` thay vì `1`.
